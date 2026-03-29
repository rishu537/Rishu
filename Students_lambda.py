students = [
    {"name": "Aman",   "city": "Delhi",   "marks": 85, "fees_paid": True},
    {"name": "Sneha",  "city": "Mumbai",  "marks": 92, "fees_paid": False},
    {"name": "Rohan",  "city": "Delhi",   "marks": 45, "fees_paid": True},
    {"name": "Priya",  "city": "Delhi",   "marks": 78, "fees_paid": False},
    {"name": "Karan",  "city": "Mumbai",  "marks": 60, "fees_paid": True},
    {"name": "Anjali", "city": "Delhi",   "marks": 95, "fees_paid": True},
]

city = list(filter(lambda x:x["city"] == "Delhi", students))
fees = list(filter(lambda x:x["fees_paid"], city))
status = list(filter(lambda x:x["marks"] >= 50, fees))
new_key = list(map(lambda x: {**x, "grade" : "A" if x["marks"] >= 90 else "B" if x["marks"] >= 75 else "C"}, status))
sort_marks = sorted(new_key, key = lambda x:x["marks"], reverse = True)

for i in sort_marks:
 print(i)