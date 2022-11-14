import requests
import pandas as pd


url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2022014?playerNameLike=&playerPosition=&teamId="

# 1) Copy as cURL from api link
# 2) Import in Postman
# 3) Paste in Raw text
# 4) And copy code for Python requests
headers = {
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'x-media-mis-token': 'f72603b067586494b973b07d63fe3379',
    'Referer': 'https://www.afl.com.au/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'Cookie': 'JSESSIONID=975FB6FDDF5426195DBE865744DCC1FE'
}


def get_data():
    response = requests.get(url, headers=headers)

    players_data = response.json()

    # with open('afl_data.json', 'w') as file:
    #     data_json = json.dumps(players_data, indent=4, ensure_ascii=False)
    #     file.write(data_json)

    players_info_list = []
    for player in players_data['players']:
        players_info_list.append({
            'full_name': player['playerDetails']['givenName'] + player['playerDetails']['surname'],
            'age': player['playerDetails']['age'],
            'photoURL': player['playerDetails']['photoURL'],
            'player_team': player['team']['teamName'],
            'games_played': player['gamesPlayed']
        })

    return players_info_list


def to_scv(players_data: list):
    df = pd.DataFrame(players_data)
    df.to_csv('players_data.csv', index=False)


def main():
    data = get_data()
    to_scv(data)


if __name__ == '__main__':
    main()
