products = [
    {"name": "Laptop",   "category": "Electronics", "price": 75000, "stock": 10},
    {"name": "Shirt",    "category": "Clothing",    "price": 1500,  "stock": 0},
    {"name": "Phone",    "category": "Electronics", "price": 25000, "stock": 5},
    {"name": "Pants",    "category": "Clothing",    "price": 2000,  "stock": 3},
    {"name": "Tablet",   "category": "Electronics", "price": 35000, "stock": 0},
    {"name": "Earbuds",  "category": "Electronics", "price": 5000,  "stock": 8},
]
category = list(filter(lambda x:x["category"] == "Electronics", products))
In_stock = list(filter(lambda x:x ["stock"] > 0, category))
discount = list(map(lambda x: {**x, "price" :x["price"] * 0.85}, In_stock))
price = list(sorted(discount, key = lambda x:x["price"]))

for i in price:
    print(i)