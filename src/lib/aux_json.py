import json


def read_json(json_path: str) -> dict:
    with open(json_path, 'r') as json_file:
        data = json_file.read()

    obj = json.loads(data)

    return obj


if __name__ == '__main__':
    print('this is a library. You cann call this function in your project')
