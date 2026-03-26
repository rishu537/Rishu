import json

with open("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    word = json.load(f)

for customer in word:
    city = customer["address"]["city"]
    if city == "Mumbai":
        print(customer["name"], city)