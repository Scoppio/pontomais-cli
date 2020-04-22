import requests
import json
from pontomais import API_ROOT, CREDENTIAL_FILE


def login(credentials):
    r = requests.post(API_ROOT+"/auth/sign_in", json=credentials).json()
    cred = {"token":  r["token"], "client_id":  r["client_id"], "email": r["data"]["email"]}

    with open(CREDENTIAL_FILE, "w") as f:
        f.write(json.dumps(cred))


if __name__ == "__main__":
    with open("profile.json", "r") as f:
        credential = json.load(f)

    my_credential = {
        "login": credential["login"],
        "password": credential["password"]
    }
    login(my_credential)