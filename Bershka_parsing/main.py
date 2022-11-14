import json
import csv
import requests
from bs4 import BeautifulSoup


def get_card_less_price(url: str, price: int):
    response = requests.get(url).text

    soup = BeautifulSoup(response, 'lxml')

    cards = soup.find_all('div', class_='goods-tile__inner')
    info = []
    for i in range(len(cards)):
        title = cards[i].find('span', class_='goods-tile__title').text.replace('\xa0•\xa0', '').strip()
        price_card = int(cards[i].find('span', class_='goods-tile__price-value').text.strip().replace(u'\xa0', ''))

        if price_card < price:
            info.append({'title': title, 'price': price_card})

    return info


def to_json(info: list):
    with open('data.json', 'w') as file:
        json.dump(info, file, ensure_ascii=False, indent=4)


def to_csv(info: list):
    csv_columns = ['title', 'price']
    with open('data.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        for data in info:
            writer.writerow(data)


def main():
    to_json(get_card_less_price('https://rozetka.com.ua/mugskie-polo/c4637815/', 400))
    to_csv(get_card_less_price('https://rozetka.com.ua/mugskie-polo/c4637815/', 400))


if __name__ == '__main__':
    main()
