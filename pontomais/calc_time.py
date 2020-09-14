import json
from datetime import datetime

import requests

from pontomais import API_ROOT, CREDENTIAL_FILE

LUNCH_TIME = 1  # Hours

credential = None


def main():
    calculate()


def calculate():
    cards = time_cards()

    if len(cards) == 3:
        _calculate_3_cards(cards)
    elif len(cards) in (1, 2):
        _calculate_fallback(cards)
    else:
        print("Unsupported number of timecards: {}".format(len(cards)))
        return


def time_cards():
    global credential
    with open(CREDENTIAL_FILE, "r") as f:
        credential = json.load(f)

    cards = request(today())['work_day']['time_cards']
    if not cards:
        print("No timecards today.")
        return
    return cards


def _calculate_fallback(cards):
    t0 = convert(cards[0])
    ttl = lambda total: mins_to_str(t0 + 60*total + 60*LUNCH_TIME)
    print(" 8h shift -> {}".format(ttl(8)))
    print("10h shift -> {}".format(ttl(10)))


def _calculate_3_cards(cards):
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
    r = requests.get(url, headers=headers)

    if 200 <= r.status_code < 300:
        return r.json()
    else:
        print(r.status_code, r.text)
        exit(1)


if __name__ == "__main__":
    with open(CREDENTIAL_FILE, "r") as f:
        credential = json.load(f)
    main()
