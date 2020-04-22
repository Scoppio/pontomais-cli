import click
import json
from pontomais.login import login as p_login


@click.group()
def cli():
    pass


@cli.command("login")
@click.option('--login', required=False)
@click.option('--address', required=False)
@click.option('--latitude', type=click.FloatRange(-90, 90), required=False)
@click.option('--longitude', type=click.FloatRange(-180, 180), required=False)
@click.option('--json-profile', required=False, type=click.File('r'))
@click.password_option(confirmation_prompt=False)
def get_credentials(login, address, latitude, longitude, json_profile, password):
    """
    if using a json profile to provide the profile, you do not require to add the password on it, the
    password will be asked to be input in a safe manner in this app

    :param login: either CPF or email
    :param address: Address of where you are working
    :param latitude: Latitude of the place you are currently working from
    :param longitude: Longitude of the place you are currently working from
    :param json_profile: a json file with login, address, latitude and longitude already on
    :param password: your password
    :return:
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
    click.echo('Calcular tempo')


@cli.command()
def register():
    click.echo("Ponto registrado")


if __name__ == "__main__":
    cli()
