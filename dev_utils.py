"""
Utility methods for development
"""
import simplejson


def dict_to_file(dict_input, filename):
    string_input = str(dict_input)
    result = string_input.replace("u'", '"')
    result = result.replace("'", '"')

    f = open(filename, 'w')
    f.write(simplejson.dumps(simplejson.loads(result), indent=4, sort_keys=True))
    f.close()


def file_to_dict(filename):
    f = open(filename, 'r')
    string = f.read()
    f.close()
    return simplejson.loads(string)
