import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

# JSON -> Python
# object -> dict
# array -> list
# string -> str
# number (int) -> int
# number (float) -> float
# true -> True
# false -> False
# null -> None

print(people_string[254])

data = json.loads(people_string)

print(data)
print(type(data))
print(type(data["people"]))

for person in data["people"]:
    print(person['name'])
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)

print(new_str)

import os

filename = os.path.join(os.path.join(os.getcwd(), 'test_files'), 'states.json')

with open(filename, 'r') as f:
    data =json.load(f)

for state in data['states']:
    print(state)
    del state['area_codes']

new_filename = os.path.join(os.path.join(os.getcwd(), 'test_files'), 'new_states.json')

with open(new_filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

from urllib.request import urlopen


# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

# data = json.loads(source)

# print(json.dumps(data, indent=2))







