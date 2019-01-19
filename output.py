
import json


def to_json_file(filename, data):
    with open(filename, 'w') as outfile:
        # pretty json is better in that case, because smaller git diff
        json.dump(json.loads(data), outfile, indent=2)
