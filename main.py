import json

from NotionAPIClient import NotionAPIClient
from objects.Page import Page
from printing import print_blocks

if __name__ == '__main__':
    client = NotionAPIClient()
    response = client.retrieve_block()
    if response is not None:
        page_json_data = json.loads(response)
        print(page_json_data)
        page = Page(page_json_data)
        print_blocks(page.blocks)
