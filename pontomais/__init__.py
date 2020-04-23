import os
from pathlib import Path

__version__ = "0.0.1"
API_ROOT = 'https://api.pontomais.com.br/api'

pontomais_dir = os.path.join(str(Path.home()), ".pontomais")

if not os.path.exists(pontomais_dir):
    os.makedirs(pontomais_dir)

CREDENTIAL_FILE =  os.path.join(pontomais_dir, ".creds")
PROFILE_FILE = os.path.join(pontomais_dir, ".profile")
