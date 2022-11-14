import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.accommodationforstudents.com/search-results?location=London&beds=0&occupancy=min&minPrice=0&maxPrice=500&latitude=51.509865&longitude=-0.118092&geo=false&page=1'
headers = {
    "user-agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_data():
    response = requests.get(base_url, headers=headers).text
    bs4 = BeautifulSoup(response, 'lxml')

    places_data = json.loads(bs4.find('script', {'id': '__NEXT_DATA__'}).text)
    all_places = places_data['props']['pageProps']['initialListings']['groups'][0]['results']

    data_list = []
    for place in all_places:

        try:
            property_type = place['property']['propertyType']
        except KeyError:
            property_type = None

        try:
            place_price = place['property']['terms']['rentPpw']['value']
        except KeyError:
            place_price = None

        try:
            total = place['property']['occupancy']['total']
            available = place['property']['occupancy']['available']
        except KeyError:
            total = None
            available = None

        try:
            place_address = place['property']['address']['area'] + ' ' + place['property']['address']['city']
        except KeyError:
            place_address = None

        try:
            place_url = 'https://www.accommodationforstudents.com' + place['property']['url']
        except KeyError:
            place_url = None

        try:
            place_images = []
            for x in range(len(place['property']['images'])):
                place_images.append(place['property']['images'][x]['url'])
        except KeyError:
            place_images = None

        data_list.append({
            'address': place_address,
            'propertyType': property_type,
            'price': place_price,
            'occupancy': [
                {'total': total},
                {'available': available}
            ],
            'url': place_url,
            'images': place_images
        })

    return data_list


def to_scv(places_list: list):
    df = pd.DataFrame(places_list)
    df.to_csv('accommodation_students.csv', index=False)


def to_json(places_list: list):
    with open('accommodation_data.json', 'w') as file:
        json.dump(places_list, file)


def main():
    data = get_data()
    to_scv(data)
    to_json(data)


if __name__ == '__main__':
    main()
