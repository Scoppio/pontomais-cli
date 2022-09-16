import json

import requests

from pontomais import API_ROOT, CREDENTIAL_FILE, PROFILE_FILE


def login(credentials):
    
    req = requests.post(API_ROOT+"/auth/sign_in", json=credentials)

    if req.status_code >= 500 :
        raise Exception(req.text)

    r = req.json()

    if(req.status_code >= 400):
        raise Exception(r["error"])

    if "email" in r["data"]:
        email = r["data"]["email"]
    else:
        email = r["data"]["login"]

    cred = {"token":  r["token"], "client_id":  r["client_id"], "email": email}


    if "password" in credentials:
        credentials.pop("password")

    with open(CREDENTIAL_FILE, "w") as f:
        f.write(json.dumps(cred))
    with open(PROFILE_FILE, "w") as f:
        f.write(json.dumps(credentials))


if __name__ == "__main__":
    with open("profile.json", "r") as f:
        credential = json.load(f)

    my_credential = {
        "login": credential["login"],
        "password": credential["password"]
    }
    login(my_credential)
