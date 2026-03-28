students = [
    {"name": "Aman",   "marks": 85, "grade": "B"},
    {"name": "Sneha",  "marks": 92, "grade": "A"},
    {"name": "Rohan",  "marks": 45, "grade": "F"},
    {"name": "Priya",  "marks": 78, "grade": "B"},
    {"name": "Karan",  "marks": 60, "grade": "C"},
    {"name": "Anjali", "marks": 95, "grade": "A"},
]

Pass = list(filter(lambda x:x["marks"] >= 50, students))
result_list = list(map(lambda x: {**x, "result": "Pass"}, Pass))
sorted_list = list(sorted(result_list, key = lambda x:x["marks"], reverse = True))

for name in sorted_list:
    print(name)