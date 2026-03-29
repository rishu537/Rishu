transactions = [
    {"id": 1, "user": "Ravi",   "type": "credit", "amount": 5000,  "verified": True},
    {"id": 2, "user": "Sneha",  "type": "debit",  "amount": 2000,  "verified": False},
    {"id": 3, "user": "Karan",  "type": "credit", "amount": 15000, "verified": True},
    {"id": 4, "user": "Pooja",  "type": "credit", "amount": 8000,  "verified": False},
    {"id": 5, "user": "Arjun",  "type": "debit",  "amount": 3000,  "verified": True},
    {"id": 6, "user": "Neha",   "type": "credit", "amount": 12000, "verified": True},
]

transaction = list(filter(lambda x:x["type"] == "credit", transactions))
verified_status = list(filter(lambda x:x["verified"], transaction))
amount = list(map(lambda x: {**x, "bonus" : x["amount"] * 0.05}, verified_status))
Sort = sorted(amount, key = lambda x:x["amount"], reverse = True)

for i in Sort:
    print(i)