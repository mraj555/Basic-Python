import json

person = '{"name": "Bob", "languages": ["English", "Hindi"]}'
person_dict = json.loads(person)

print(person_dict)
print(person_dict['languages'])

with open("data.json") as f:
    data = json.load(f)

print(data)
