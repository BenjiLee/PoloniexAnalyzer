"""
Utility methods for development
"""
import simplejson


def dict_to_file(dict_input):
    string_input = str(dict_input)
    result = string_input.replace("u'", '"')
    result = result.replace("'", '"')

    f = open('dump.json', 'w')
    f.write(simplejson.dumps(simplejson.loads(result), indent=4, sort_keys=True))
    f.close()
