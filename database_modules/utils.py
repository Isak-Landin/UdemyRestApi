import json
import requests
from GeneralUtils.decorators import reformatting


@reformatting
def response_decoder(response: requests.Response) -> dict:
    return json.loads(response.content.decode('utf-8'))


@reformatting
def get_count_in_dict(decoded_dict: dict):
    return count if (count := decoded_dict.get('count')) else {}


@reformatting
def get_data_in_dict(decoded_dict: dict):
    data = decoded_dict.get('data', [])
    return data[0] or {}


@reformatting
def get_rows_in_dict(decoded_dict: dict):
    rows = decoded_dict.get('rows', [])
    return rows[0] or {}

