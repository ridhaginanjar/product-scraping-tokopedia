import json


def export(data):
    with open(f'export.json', 'w', ) as output:
        json.dump(data, output, indent=4)