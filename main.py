import json

from NotionAPIClient import NotionAPIClient
from printing import print_block

if __name__ == '__main__':
    client = NotionAPIClient()
    response = client.retrieve_block()
    if response is not None:
        block_json_data = json.loads(response)
        print_block(json.dumps(block_json_data, indent=4))
