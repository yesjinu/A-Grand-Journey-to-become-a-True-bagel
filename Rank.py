import requests
import json
URL_update_rank = 'http://54.180.140.113:10001/jinu/update_rank'
URL_get_rank = 'http://54.180.140.113:10001/jinu/get_rank'

def get_rank():
    response = requests.post(URL_get_rank).json()['data']
    top_10_rank = []
    if len(response) > 10:
        for i in range(10):
            player_name = response[i]['name']
            player_score = response[i]['score']
            temp_info = (player_name, player_score)
            top_10_rank.append(temp_info)
    else:
        for player in response:
            player_name = player['name']
            player_score = player['score']
            temp_info = (player_name, player_score)
            top_10_rank.append(temp_info)
    return top_10_rank


def update_rank(name, score):
    body = {
        'name': f'{name}',
        'score': f'{score}'
    }

    # res = requests.post(URL_update_rank, data=json.dumps(body)).json()
    data = json.dumps(body)
    files = {
        'data': (None, data)
    }
    request = requests.Request('POST', URL_update_rank, files=files).prepare()
    session = requests.Session()
    res = session.send(request)
    print("res", res)

