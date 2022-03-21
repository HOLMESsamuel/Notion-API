import json

from api_requests import retrieve_block


def print_block():
    block_json_data = json.loads(retrieve_block())
    print(json.dumps(block_json_data, indent=4))


if __name__ == '__main__':
    print_block()
