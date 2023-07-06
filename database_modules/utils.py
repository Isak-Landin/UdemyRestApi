import json
import requests


def response_decoder(response: requests.Response) -> dict:
    return json.loads(response.content.decode('utf-8'))


def get_count_in_dict(decoded_dict: dict):
    count = None
    try:
        count = decoded_dict.get('count')
        if not count:
            raise KeyError
    except (KeyError, AttributeError):
        return {}

    return count


def get_data_in_dict(decoded_dict: dict):
    data = None
    try:
        data = decoded_dict.get('data')[0]
        if not data:
            raise KeyError
    except (KeyError, AttributeError):
        return {}
    except IndexError:
        print('data', data)

    print('Data contents for db request: ', data)
    return data


def get_rows_in_dict(decoded_dict: dict):
    try:
        rows = decoded_dict.get('rows')[0]
        if not rows:
            raise KeyError
    except (KeyError, AttributeError):
        return {}
    return rows
