import json
import requests
from requests import Response
from GeneralUtils.decorators import standard_procedure


@standard_procedure
def response_content_decoder(response: Response) -> dict:
    return json.loads(response.content.decode('utf-8'))


@standard_procedure
def get_count_in_dict(decoded_dict: dict):
    count = decoded_dict.get('count')
    return count if count or count == 0 else {}


@standard_procedure
def get_data_in_dict(decoded_dict: dict):
    data = decoded_dict.get('data', [])
    return data[0] or {}


@standard_procedure
def get_rows_in_dict(decoded_dict: dict):
    rows = decoded_dict.get('rows', [])
    return rows[0] or {}


@standard_procedure
def get_status_code_of_response(response: dict):
    return response.status_code if isinstance(response, Response) else None

