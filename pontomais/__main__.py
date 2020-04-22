import json

import click

from pontomais.calc_time import main as p_calculate
from pontomais.clockin import main as p_register
from pontomais.login import login as p_login


@click.group()
def cli():
    pass


@cli.command("login")
@click.option('--login', required=False, help="either CPF or email")
@click.option('--address', required=False, help="Address of where you are working")
@click.option('--latitude', type=click.FloatRange(-90, 90), required=False,
              help="Latitude of the place you are currently working from")
@click.option('--longitude', type=click.FloatRange(-180, 180), required=False,
              help="Longitude of the place you are currently working from")
@click.option('--json-profile', required=False, type=click.File('r'),
              help="a json file with login, address, latitude and longitude already on")
@click.password_option(confirmation_prompt=False)
def get_credentials(login, address, latitude, longitude, json_profile, password):
    """
    Generate a credential file necessary to do almost any action with this client

    if using a json profile to provide the profile, you do not require to add the password on it, the
    password will be asked to be input in a safe manner in this app

    """
    if json_profile:
        profile = json.load(json_profile)
    else:
        if not login or not latitude or not longitude or not address:
            raise RuntimeError("Missing arguments, must provide login, latitude, longitude, address and password")
        profile = {"login": login, "latitude": latitude, "longitude": longitude, "address": address}
    profile["password"] = password

    p_login(profile)


@cli.command()
def calctime():
    """
    Calculates at which time you need to clock out of work
    """
    p_calculate()


@cli.command()
def register():
    """
    Clocks in and out of the job
    """
    p_register()


if __name__ == "__main__":
    cli()
