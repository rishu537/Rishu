import logging

employees = [
    {"name": "Ravi",   "salary": 15000},
    {"name": "Sneha",  "salary": 55000},
    {"name": "Karan",  "salary": 8000},
    {"name": "Pooja",  "salary": 32000},
    {"name": "Arjun",  "salary": 75000},
]

logging.basicConfig(
    filename = "Salary_check.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programe Started")

for emp in employees:
    if emp["salary"] < 10000:
        logging.error(f"{emp['name'] } salary is {emp['salary']} - Underpaid")
    elif emp["salary"] < 50000:
        logging.warning(f"{emp['name']} salary is {emp['salary']} - Average Paid")
    else:
        logging.info(f"{emp['name']} salary is {emp['salary']} - Well paid")

logging.info("Program Complete")