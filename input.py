import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['DEFAULT']['token']
USERNAME = config['DEFAULT']['account_name']
HEADER = {'X-Auth-Token': TOKEN}