import json

with open("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    data = json.load(f)
    for customer in data:
        print(customer["name"], "->", customer["contact"]["email"])