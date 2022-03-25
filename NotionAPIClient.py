import configparser

from NotionAPISession import NotionAPISession
from exception import handle_error

# TODO : separate base url
base_url = "https://api.notion.com/v1/blocks/"


class NotionAPIClient(object):

    def __init__(self):
        self.session = NotionAPISession()

    def retrieve_block(self, id):
        url = base_url + id + "/children?page_size=100"
        response = self.session.request("GET", url, headers=self.session.headers)
        if response.status_code > 400:
            handle_error(response.text)
        else:
            return response.text
