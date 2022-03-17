import requests
import configparser

base_url = "https://api.notion.com/v1/blocks/"

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
    url = base_url + ids["personal_home_page_id"] + "/children?page_size=100"
    response = requests.request("GET", url, headers=headers)
    return response.text
