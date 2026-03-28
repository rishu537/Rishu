orders = [
    {"order_id": 1, "product": "Laptop",  "amount": 75000, "status": "delivered"},
    {"order_id": 2, "product": "Phone",   "amount": 15000, "status": "pending"},
    {"order_id": 3, "product": "Tablet",  "amount": 25000, "status": "delivered"},
    {"order_id": 4, "product": "Monitor", "amount": 12000, "status": "cancelled"},
    {"order_id": 5, "product": "Mouse",   "amount": 999,   "status": "delivered"},
]

status = list(filter(lambda x:x["status"] == "delivered", orders))
discount = list(map(lambda x :{**x, "amount":x["amount"] * 0.9}, status))

for orderss in discount:
    print(orderss)