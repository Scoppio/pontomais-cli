# Pontomais-CLI

Ferramenta para registrar ponto e outras funcionalidades

## Como instalar

Baixe esse repositório para seu computador (por zip ou com git clone) e então 
rode o seguinte comando dentro da pasta do programa

```shell script
pip3 install . 
```

## Como usar

Uma vez instalado, basta usar é muito simples, no terminal rode o commando:

```shell script
ptm --help
```

o resultado deve ser o seguinte

```shell script
 % ptm --help
Usage: ptm [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  calctime  Calculates at which time you need to clock out of work
  login     Generate a credential file necessary to do almost any action...
  register  Clocks in and out of the job
```

Pra fazer o login basta:
```shell script
ptm login --json-profile <ARQUIVO> 

# or

ptm login --login [LOGIN] --latitude [LAT] --longitude [LON] --address [ENDEREÇO]
```

Claro que o help também funciona em qualquer um dos commandos

```shell script
 % ptm login --help

  Generate a credential file necessary to do almost any action with this
  client

  if using a json profile to provide the profile, you do not require to add
  the password on it, the password will be asked to be input in a safe
  manner in this app

Options:
  --login TEXT             either CPF or email
  --address TEXT           Address of where you are working
  --latitude FLOAT RANGE   Latitude of the place you are currently working
                           from

  --longitude FLOAT RANGE  Longitude of the place you are currently working
                           from

  --json-profile FILENAME  a json file with login, address, latitude and
                           longitude already on

  --password TEXT
  --help                   Show this message and exit.
```