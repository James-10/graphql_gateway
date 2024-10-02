import yaml
import dotenv
import os

dotenv.load_dotenv()

class Config:
    env = os.getenv('ENVIRONMENT')
    appname = "graphql_gateway"

def load_config(config_file='config.yml'):
    with open(config_file, 'r') as file:
        config_data = dict(yaml.safe_load(file))

    for key, value in config_data.items():
        if isinstance(value, dict):
            setattr(Config, key, value)

load_config()