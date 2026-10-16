import urllib.request

import json

url = "http://jsonplaceholder.typicode.com/todos/1"

with urllib.request.urlopen(url) as raw_json:
    converted_json = json.load(raw_json)

print(converted_json)
print(type(converted_json))