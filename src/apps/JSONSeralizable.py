import json

class JSONSerializable:

    @classmethod
    def to_dict(cls, application, app_slots):
        result = dict()
        properties = app_slots
        for prop in properties:
            prop = prop[1:]
            if isinstance(getattr(application, prop), list):
                values_set = getattr(application, prop)
                i = 0
                values_dict = dict()
                for value_loop in values_set:
                    values_dict.update({i: value_loop.value})
                    i += 1
                value = values_dict
            elif prop == "platform":
                platform_value = getattr(application, prop)
                value = cls.to_dict(platform_value, platform_value.fields)
            else:
                value = getattr(application, prop)
            result.update({prop: value})
        return result

    @classmethod
    def to_json(cls, application, application_slots):
        return json.dumps(cls.to_dict(application, application_slots), separators=(',', ':'), indent=4)

    @classmethod
    def write_to_json(cls, application, application_slots: tuple, path: str):
        with open(path, "a") as fp:
            json.dump(cls.to_dict(application, application_slots), fp, separators=(',', ':'), indent=4)
