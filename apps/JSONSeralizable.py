import json
class JSONSerializable:

    @staticmethod
    def to_json(dictionary: dict):
        return json.dumps(dictionary, separators=(',', ':'), indent=4)

    @staticmethod
    def write_to_json(dictionary: dict, path: str):
        with open("JSONs.txt", "a") as fp:
            json.dump(dictionary, fp, separators=(',', ':'), indent=4)
