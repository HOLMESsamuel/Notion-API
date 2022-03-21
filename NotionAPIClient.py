import configparser

from NotionAPISession import NotionAPISession
from exception import handle_error

base_url = "https://api.notion.com/v1/blocks/"

config_obj = configparser.ConfigParser()
config_obj.read('./config.ini')
ids = config_obj["ids"]


class NotionAPIClient(object):

    def __init__(self):
        self.session = NotionAPISession()

    def retrieve_block(self):
        url = base_url + ids["personal_home_page_id"] + "/children?page_size=100"
        response = self.session.request("GET", url, headers=self.session.headers)
        if response.status_code > 400:
            handle_error(response.text)
        else:
            return response.text
