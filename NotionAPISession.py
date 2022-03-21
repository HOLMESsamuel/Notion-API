import configparser

import requests


class NotionAPISession(requests.Session):

    def __init__(self):
        super(NotionAPISession, self).__init__()

        config_obj = configparser.ConfigParser()
        config_obj.read('./config.ini')
        tokens = config_obj["tokens"]
        versions = config_obj["versions"]

        self.headers.update({
            "Accept": "application/json",
            "Notion-Version": versions["notion_version"],
            "Authorization": tokens["header_prefix"] + " " + tokens["internal_integration_token"]
        })
