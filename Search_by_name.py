import json

with open("/Users/rishu/CodePractice/python-practice/customers.json", "r") as f:
    data = json.load(f)

name = input("Enter a name: ")

found = False
for customer in data:
    if customer["name"] == name:
        print("Name:", customer["name"])
        print("Address:", customer["address"])
        print("Phone No:", customer["contact"]["mobile"])
        print("Email:", customer["contact"]["email"])
        found = True
        break

if found == False:
    print("Customer not found")
