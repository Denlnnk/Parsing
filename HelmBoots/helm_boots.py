from requests_html import HTMLSession

session = HTMLSession()
base_url = 'https://helmboots.com'

products_data_list = []


def get_all_product_links():
    response = session.get('https://helmboots.com/collections/shop')
    response.html.render(timeout=30)

    all_products = response.html.find('div.gc-product')

    return [base_url + product.find('a.grid-view-item__link', first=True).attrs['href'] for product in all_products]


def get_product_data(product_links: list):
    count = 1
    for link in product_links:
        response = session.get(link)
        response.html.render(timeout=30)

        name = response.html.find('h1.product-single__title.libre', first=True).text
        price = response.html.find('span#ProductPrice-product-with-banner-template', first=True).text
        try:
            rating = response.html.find('span.stamped-summary-text-1', first=True).text
        except:
            rating = 'none'
        try:
            reviews = response.html.find('span.stamped-summary-text', first=True).text
        except:
            reviews = 'none'
        img_src = base_url + response.html.find('img#FeaturedImage-product-with-banner-template', first=True).attrs['src']
        products_data_list.append({
            'name': name,
            'price': price,
            'rating': rating,
            'reviews': reviews,
            'link': link,
            'img_src': img_src,
        })
        count += 1
        print(f'Collected {count} items')
    print(products_data_list)
    return products_data_list


def main():
    product_links = get_all_product_links()
    get_product_data(product_links)


if __name__ == '__main__':
    main()
