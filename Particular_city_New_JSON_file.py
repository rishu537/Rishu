import json

with open("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    load = json.load(f)

mumbai_customer = []

for customer in load:
    if customer["address"]["city"] == "Chennai":
        mumbai_customer.append(customer)

with open("/Users/rishu/CodePractice/python-practice/demo.json", "w") as f:
    json.dump(mumbai_customer, f, indent=4)