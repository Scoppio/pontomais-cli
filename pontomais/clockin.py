# ttl.py - Calculates when to finish your workday based on data from Pontomais
# Setup: insert auth in function request() with the instructions there and run.
import json
from datetime import datetime
from uuid import uuid4

import requests

from pontomais import API_ROOT, CREDENTIAL_FILE, PROFILE_FILE


def main():
    with open(CREDENTIAL_FILE, "r") as f:
        credential = json.load(f)

    with open(PROFILE_FILE, "r") as f:
        profile = json.load(f)
    address = create_my_address_info(profile)
    request(address, credential)


def create_my_address_info(_pr):
    return {
        "time_card": {
            "latitude": _pr["latitude"],
            "longitude": _pr["longitude"],
            "address": _pr["address"],
            "reference_id": None,
            "original_latitude": _pr["latitude"],
            "original_longitude": _pr["longitude"],
            "original_address": _pr["address"],
            "location_edited": True,
            "accuracy": 9590
        },
        "_path": '/meu_ponto/registro_de_ponto',
        "_device": {
            "browser": {
                "name": 'Chrome',
                "version": '80.0.3987.163',
                "versionSearchString": 'Chrome'
            }
        },
        "_appVersion": '0.10.32'
    }
    

def get_common_headers():
    return {
        'authority': 'api.pontomais.com.br',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'api-version': '2',
        'if-modified-since': 'Mon, 26 Jul 1997 05:00:00 GMT',
        'origin': 'https://app.pontomaisweb.com.br',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }

def request(address, credential):
    # Take from the api/time_card_control/current/work_days/ request
    # headers in Pontomais
    headers = get_common_headers()
    headers.update({
        'access-token': credential["token"],
        'token-type': 'Bearer',
        'client': credential["client_id"],
        'uid': credential["email"],
        'uuid': str(uuid4())
    })

    url = "{}/time_cards/register".format(API_ROOT)
    r = requests.post(url, headers=headers, json=address)
    print(datetime.now(), "- Status code:", r.status_code)



if __name__ == "__main__":
    main()
