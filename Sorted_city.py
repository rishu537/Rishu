import json

with open("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    data = json.load(f)

for customer in sorted(data, key = lambda x:x["address"]["city"]):
    print(customer["name"], "->", customer["address"]["city"])