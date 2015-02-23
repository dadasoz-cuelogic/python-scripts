
def expand(key, value):
    if isinstance(value, dict):
        return [ (key + '.' + k, v) for k, v in flatten_dict(value).items() ]
    else:

        return [ (key, value) ]


def flatten_dict(d):
    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})