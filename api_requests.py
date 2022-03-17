import requests
import configparser

url = "https://api.notion.com/v1/blocks/be49b29265bb43808cbc3953f5f5cb2f/children?page_size=100"

config_obj = configparser.ConfigParser()
config_obj.read('./config.ini')
tokens = config_obj["tokens"]
ids = config_obj["ids"]
versions = config_obj["versions"]

headers = {
    "Accept": "application/json",
    "Notion-Version": versions["notion_version"],
    "Authorization": "Bearer " + tokens["internal_integration_token"]
}


def retrieve_block():
    response = requests.request("GET", url, headers=headers)
    print(response.text)
