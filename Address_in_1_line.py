import json

with open("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    data = json.load(f)

    for customers in data:
        address = customers["address"]
        print(customers["name"], "->", address["address1"], ",", address["address2"], ",", address["city"], ",", address["state"], ",", address["pincode"])