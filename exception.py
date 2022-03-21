import json


# handle error responses

def handle_error(resp):
    error_json_data = json.loads(resp)
    print(json.dumps(error_json_data, indent=4))
