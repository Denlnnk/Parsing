import requests
from bs4 import BeautifulSoup

url = 'https://helmboots.com/collections/shop'
base_url = 'https://helmboots.com/'
headers = {
    "user-agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_all_products_links():
    response = requests.get(url, headers=headers).content
    bs4 = BeautifulSoup(response, 'lxml')

    all_product = bs4.findAll('div', class_='gc-product')

    all_product_links = []
    for links in all_product:
        all_product_links.append(base_url + links.find('a', class_='grid-view-item__link')['href'])

    return all_product_links


def get_data(products_links: list):
    products_info_list = []
    for product_link in products_links[:1]:
        response = requests.get(product_link, headers=headers).content
        bs4 = BeautifulSoup(response, 'lxml')

        images_links = bs4.findAll('div', class_='image-wrap')

        images_links_list = [links.find('img')['src'] for links in images_links]

        print(bs4.find('div', class_='summary-overview'))
        products_info_list.append({
            'name': bs4.find('h1', class_='product-single__title libre').text.strip(),
            'price': bs4.find('span', id='ProductPrice-product-with-banner-template').text.strip(),
            'images': images_links_list,
            'rating': 0
        })

    return products_info_list


def main():
    all_links = get_all_products_links()
    get_data(all_links)


if __name__ == '__main__':
    main()
