
import json


def to_json_file(filename, data):
    with open(filename, 'w') as outfile:
        # pretty json is better in that case, because smaller git diff
        prettyJson = json.dumps(json.loads(data), indent=2)
        json.dump(prettyJson, outfile)
