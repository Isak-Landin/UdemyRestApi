import json
import requests


def response_decoder(response: requests.Response) -> dict:
    return json.loads(response.content.decode('utf-8'))


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

    return data


def get_rows_in_dict(decoded_dict: dict):
    try:
        rows = decoded_dict.get('rows')[0]
        if not rows:
            raise KeyError
    except (KeyError, AttributeError):
        return {}
    return rows
