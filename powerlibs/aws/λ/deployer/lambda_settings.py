import json

MANDATORY_SETTINGS = ('FunctionName', 'Handler', 'Role', 'Runtime')


def load_settings(filepath):
    with open(filepath, 'r') as f:
        settings = json.loads(f.read())
    for key in MANDATORY_SETTINGS:
        try:
            assert key in settings
        except AssertionError:
            raise KeyError('{} not found in the settings JSON.'.format(key))
    return settings
