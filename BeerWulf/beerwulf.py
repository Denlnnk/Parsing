import pandas as pd
import requests

baseurl = 'https://www.beerwulf.com'

headers = {
    "user-agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_data():
    items_list = []
    for x in range(1, 5):
        response = requests.get(f'https://www.beerwulf.com/en-GB/api/search/searchProducts?routeQuery=c&page={x}',
                                headers=headers)
        data = response.json()

        # with open('data.json', 'w') as file:
        #     data_json = json.dumps(data, indent=4, ensure_ascii=False)
        #     file.write(data_json)
        for item in data['items']:
            try:
                product_img_url = baseurl + item['images'][0]['image']
            except KeyError:
                product_img_url = None
            items_list.append({
                'title': item['title'],
                'product_img_url': product_img_url,
                'in_stock': item['inStock'],
                'alcoholPercentage': item['alcoholPercentage'],
                'price': item['displayInformationPrice']['price'].strip()
            })

    return items_list


def to_csv(product_info: list):
    df = pd.DataFrame(product_info)
    df.to_csv('static/BeerWulf_data.csv', index=False)


def main():
    data = get_data()
    to_csv(data)


if __name__ == '__main__':
    main()
