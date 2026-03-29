employees = [
    {"name": "Ravi",   "dept": "IT",      "salary": 55000},
    {"name": "Sneha",  "dept": "HR",      "salary": 38000},
    {"name": "Karan",  "dept": "IT",      "salary": 72000},
    {"name": "Pooja",  "dept": "Finance", "salary": 45000},
    {"name": "Arjun",  "dept": "IT",      "salary": 61000},
    {"name": "Neha",   "dept": "HR",      "salary": 29000},
]

department = list(filter(lambda x:x["dept"] == "IT", employees))
salary_hike = list(map(lambda x:{**x, "salary" : x["salary"] * 1.2}, department))
Sort_salary = list(sorted(salary_hike, key = lambda x:x["salary"], reverse = True))

for i in Sort_salary:
    print(i)