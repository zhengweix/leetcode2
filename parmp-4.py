def flatten_dictionary(nested_dict):
    '''
    Flatten a Dictionary
    Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it.
    If a certain key is empty, it should be excluded from the output (see e in the example below).
    input:  dict = {
                "Key1" : "1",
                "Key2" : {
                    "a" : "2",
                    "b" : "3",
                    "c" : {
                        "d" : "3",
                        "e" : {
                            "" : "1"
                        }
                    }
                }
            }
    output: {
                "Key1" : "1",
                "Key2.a" : "2",
                "Key2.b" : "3",
                "Key2.c.d" : "3",
                "Key2.c.e" : "1"
            }
    '''

    def flatten_dict(d, parent_key):
        items = []
        for k, v in d.items():
            new_key = parent_key + '.' + k if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key).items())
            else:
                items.append((new_key, v))
        return dict(items)

    return flatten_dict(nested_dict, '')
dictionary = {
    "Key1" : "1",
    "Key2" : {
        "a" : "2",
        "b" : "3",
        "c" : {
            "d" : "3",
            "e" : {
                "" : "1"
            }
        }
    }
}
print(flatten_dictionary(dictionary))