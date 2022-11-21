import requests
import pandas as pd
from bs4 import BeautifulSoup


baseurl = 'https://www.thewhiskyexchange.com'

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def all_product_links():
    product_links = []
    for x in range(1, 2):
        response = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}').content
        bs4 = BeautifulSoup(response, 'lxml')
        product_list = bs4.findAll('li', class_='product-grid__item')
        for item in product_list:
            info_links = item.find('a', class_='product-card')
            product_links.append(baseurl + info_links['href'])

    return product_links


def product_info(product_links: list):
    products_info = []
    count = 0
    for link in product_links:
        count += 1
        response = requests.get(link, headers=headers).content
        bs4 = BeautifulSoup(response, 'lxml')
        name = bs4.find('h1', class_='product-main__name').text.strip()
        price = bs4.find('p', class_='product-action__price').text.strip()
        try:
            rating = bs4.find('p', class_='review-overview__content').find('span').text.strip()
        except AttributeError:
            rating = 'no rating'
        try:
            reviews = bs4.find('span', class_='review-overview__count').text.strip().replace('&nbsp', '').replace(
                u'\xa0', '')
        except AttributeError:
            reviews = 'no views'
        try:
            percent_alcohol = bs4.find('p', class_='product-main__data').text.strip()
        except AttributeError:
            percent_alcohol = None

        products_info.append({
            'name': name,
            'percent_alcohol': percent_alcohol,
            'rating': rating,
            'price': price,
            'reviews': reviews
        })
        print(f'Collected {count} pages')

    return products_info


def to_scv(products_info: list):
    # csv_columns = ['name', 'rating', 'price', 'reviews']
    # with open('japanise_wiskey1.csv', 'w') as csv_file:
    #     writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    #     writer.writeheader()
    #     for key, value in product_info.items():
    #         row = {'name': key}
    #         row.update(value)
    #         writer.writerow(row)
    df = pd.DataFrame(products_info)
    df.to_csv('static/japanise_wiskey.csv', index=False)


def main():
    product_links = all_product_links()
    products_info = product_info(product_links)
    to_scv(products_info)


if __name__ == '__main__':
    main()
