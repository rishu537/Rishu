import json

with open ("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    lines = json.load(f)

count = {}

for customer in lines:
    city = customer["address"]["city"]
    if city in count:
        count[city] += 1
    else:
        count[city] = 1

for city in count:
    print(city, "=", count[city])