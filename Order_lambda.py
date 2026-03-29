orders = [
    {"order_id": 1, "customer": "Ravi",   "city": "Mumbai",    "amount": 5000,  "status": "delivered"},
    {"order_id": 2, "customer": "Sneha",  "city": "Delhi",     "amount": 12000, "status": "pending"},
    {"order_id": 3, "customer": "Karan",  "city": "Mumbai",    "amount": 8000,  "status": "delivered"},
    {"order_id": 4, "customer": "Pooja",  "city": "Chennai",   "amount": 3000,  "status": "cancelled"},
    {"order_id": 5, "customer": "Arjun",  "city": "Mumbai",    "amount": 15000, "status": "delivered"},
    {"order_id": 6, "customer": "Neha",   "city": "Delhi",     "amount": 9000,  "status": "delivered"},
]

city = list(filter(lambda x:x["city"] == "Mumbai", orders))
status = list(filter(lambda x:x["status"] == "delivered", city))
new_key = list(map(lambda x:{**x, "tax":x["amount"] * 0.18}, status))
sort_amount = list(sorted(new_key, key = lambda x:x["amount"], reverse = True))

for i in sort_amount:
    print(i)