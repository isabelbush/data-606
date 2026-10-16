import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}

car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
print(type(car_data_json_string))

parsed_json_data = json.loads(car_data_json_string)
print(parsed_json_data)
print(type(parsed_json_data))

with open("new_json_file.json", "w") as new_json_file:
     json.dump(car_data, new_json_file)

with open("new_json_file.json") as opened_json_file:
     car = json.load(opened_json_file)
     print(car)
     print(type(car))