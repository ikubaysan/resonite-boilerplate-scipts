import configparser
import os

def load_config(section: str, filename: str = 'config.ini') -> tuple[str, int]:
    if not os.path.exists(filename):
        raise FileNotFoundError(
            f"Configuration file '{filename}' not found.\n"
            f"Please create it by copying 'config_sample.ini' and modifying it as needed."
        )

    config = configparser.ConfigParser()
    config.read(filename)

    if section not in config:
        raise ValueError(f"Missing section '{section}' in {filename}")

    host = config.get(section, 'host')
    port = config.getint(section, 'port')
    return host, port
