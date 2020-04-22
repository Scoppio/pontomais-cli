# ttl.py - Calculates when to finish your workday based on data from Pontomais
# Setup: insert auth in function request() with the instructions there and run.
import requests
from pprint import pprint
from datetime import datetime

import json

LUNCH_TIME = 1  # Hours
API_ROOT = 'https://api.pontomais.com.br/api'

with open("../credentials.json", "r") as f:
    credential = json.load(f)

def main():
    cards = request(today())['work_day']['time_cards']
    if not cards:
        print("No timecards today.")
        exit(1)

    if len(cards) == 3:
        calculate_3_cards(cards)
    elif len(cards) in (1, 2):
        calculate_fallback(cards)
    else:
        print("Unsupported number of timecards: {}".format(len(cards)))
        exit(1)


def calculate_fallback(cards):
    t0 = convert(cards[0])
    ttl = lambda total: mins_to_str(t0 + 60*total + 60*LUNCH_TIME)
    print(" 8h shift -> {}".format(ttl(8)))
    print("10h shift -> {}".format(ttl(10)))


def calculate_3_cards(cards):
    t1, t2, t3 = [convert(c) for c in cards]
    now = now_mins()

    # Calculate
    p1 = t2 - t1
    p2 = now - t3

    # Show
    ttl = lambda total: mins_to_str(now + total*60 - p1 - p2)
    print(" 8h shift -> {}".format(ttl(8)))
    print("10h shift -> {}".format(ttl(10)))


def convert(card):
    return str_to_mins(card['time'])


def str_to_mins(s):
    h, m = s.split(":")
    return 60*int(h) + int(m)


def mins_to_str(m):
    h, m = divmod(m, 60)
    return "{:02d}:{:02d}".format(h, m)


def now_mins():
    now = datetime.now()
    return 60*now.hour + now.minute


def today():
    return datetime.now().isoformat()[:10]


def request(day):
    # Take from the api/time_card_control/current/work_days/ request
    # headers in Pontomais
    headers = {
        'access-token': credential["token"],
        'client': credential["client_id"],
        'uid': credential["email"],
    }

    url = "{}/time_card_control/current/work_days/{}".format(API_ROOT, day)
    return requests.get(url, headers=headers).json()

if __name__ == "__main__":
    main()