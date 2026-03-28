customers = [
    {"name": "Arjun Shah",   "city": "Mumbai", "age": 28},
    {"name": "Priya Mehta",  "city": "Chennai", "age": 35},
    {"name": "Emily Watson", "city": "Mumbai", "age": 22},
    {"name": "Rajesh Kumar", "city": "Bangalore", "age": 40},
    {"name": "Pooja Desai",  "city": "Mumbai", "age": 31},
]

city = list(filter(lambda x:x["city"] == "Mumbai", customers))
age = list(filter(lambda x:x["age"] >= 25, city))

print(age)