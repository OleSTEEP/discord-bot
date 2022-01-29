import configparser
import os

file = os.path.join(os.path.dirname(__file__), '../config.ini')
config = configparser.ConfigParser()
config.read(file)
botconfig = config['BOTCONFIG']


def parse_token():
    return botconfig['Token']


def parse_prefix():
    return botconfig['Prefix']
