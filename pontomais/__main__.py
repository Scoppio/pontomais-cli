import json

import click

from pontomais.calc_time import main as p_calculate
from pontomais.calc_time import time_cards as p_time_cards
from pontomais.clockin import main as p_register
from pontomais.login import login as p_login

from pathlib import Path
import os
from getpass import getpass


@click.group()
def cli():
    pass


@cli.command("login")
@click.option('--login', required=False, help="either CPF or email")
@click.option('--password', required=False, help="password")
@click.option('--address', required=False, help="Address of where you are working")
@click.option('--latitude', type=click.FloatRange(-90, 90), required=False,
              help="Latitude of the place you are currently working from")
@click.option('--longitude', type=click.FloatRange(-180, 180), required=False,
              help="Longitude of the place you are currently working from")
@click.option('--profile', required=False, type=click.File('r'),
              help="a json file with login, address, latitude and longitude already on")
def get_credentials(login, address, latitude, longitude, profile, password):
    """
    Generate a credential file necessary to do almost any action with this client

    if using a json profile to provide the profile, you do not require to add the password on it, the
    password will be asked to be input in a safe manner in this app

    """
    
    if login and latitude and longitude and address:
        if not password:
            password = getpass()
        credentials = {"login": login, "latitude": latitude, "longitude": longitude, "address": address, "password":password}

    elif profile:
        credentials = json.load(profile)
    else:
        default_path = os.path.join(str(Path.home()), ".pontomais/profile.json")
        with open(default_path, "r") as f:
            credentials = json.load(f)

    if "password" not in credentials:
        credentials["password"] = getpass()

    p_login(credentials)


@cli.command("ttco")
def calctime():
    """
    Time to clock out - Calculates at which time you need to clock out of work
    """
    p_calculate()


@cli.command("cards")
def time_cards():
    """
    Time cards you clocked today
    """
    cards = p_time_cards()

    if cards is None:
        return
    for n, card in enumerate(cards):
        print("Time Card:", n)
        print(card["date"], card["time"])
        print(card["source"]["name"])
        print("---")


@cli.command("clk")
def register():
    """
    Clocks in and out of the job
    """
    p_register()


if __name__ == "__main__":
    cli()
