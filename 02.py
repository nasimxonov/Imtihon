import json

data = {
    "first_name": "John",
    "Last_name": "Doe",
    "age": 34,
    "student": False,
    "worker": True
}

def dict_to_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def file_to_dict(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

dict_to_file(data, 'data.json')

malumot = file_to_dict('data.json')

print(malumot)
