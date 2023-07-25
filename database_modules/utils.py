import json
import requests
from requests import Response
from GeneralUtils.decorators import reformatting


@reformatting
def response_content_decoder(response: Response) -> dict:
    return json.loads(response.content.decode('utf-8'))


@reformatting
def get_count_in_dict(decoded_dict: dict):
    count = decoded_dict.get('count')
    return count if count or count == 0 else {}


@reformatting
def get_data_in_dict(decoded_dict: dict):
    data = decoded_dict.get('data', [])
    return data[0] or {}


@reformatting
def get_rows_in_dict(decoded_dict: dict):
    rows = decoded_dict.get('rows', [])
    return rows[0] or {}


@reformatting
def get_status_code_of_response(response: dict):
    return response.status_code if isinstance(response, Response) else None

