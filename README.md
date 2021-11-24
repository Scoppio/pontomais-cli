# Pontomais-CLI

Ferramenta para registrar ponto e outras funcionalidades

## Como instalar

Baixe esse repositório para seu computador (por zip ou com git clone) e então 
rode o seguinte comando dentro da pasta do programa

```shell script
pip3 install . 
```

Caso o comando `ptm` não seja encontrado no seu terminal verifique se o local de instalação do pacote se encontra na variável de ambiente PATH. Executar a saída do comando abaixo pode resolver o problema para a sessão atual e adicionar este comando no arquivo `~/.bashrc` ou `~/.zshrc` pode resolver o problema permanentemente.

```shell script
echo "export PATH=$(pip3 show pontomais-cli | grep Location | cut -d' '  -f2 | sed 's/lib.*//')bin:\$PATH"
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
  clk    Clocks in and out of the job
  login  Generate a credential file necessary to do almost any action with...
  ttco   Time to clock out - Calculates at which time you need to clock out...

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

## Exemplo de arquivo PROFILE.json

```json
{
    "login": "CPF SÓ OS DIGITOS",
    "latitude": -17.0,
    "longitude": -42.0,
    "address": "Rua Sete de Março, 1009 - Ipiranga, Juazeiro do Norte - SP, 99999-999, Brasil"
}

```
