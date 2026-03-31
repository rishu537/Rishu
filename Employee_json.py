import datetime
import logging

logging.basicConfig(
    filename = "Employee.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

employees = [
    {"name": "Ravi",   "dept": "IT",      "salary": 55000, "active": True},
    {"name": "Sneha",  "dept": "HR",      "salary": 38000, "active": False},
    {"name": "Karan",  "dept": "IT",      "salary": 72000, "active": True},
    {"name": "Pooja",  "dept": "Finance", "salary": 45000, "active": True},
    {"name": "Arjun",  "dept": "IT",      "salary": 61000, "active": False},
]

today = datetime.datetime.now()
day_name = today.strftime("%A")

logging.info(f"Process Started - Today is {day_name}")

if day_name in ["Saturday", "Sunday"]:
    logging.error("Today is weekend - No processing")
else:
    active = list(filter(lambda x:x ["active"], employees))
    logging.info(f"Total active Employee: {len(active)}")

    for emp in active:
        if emp["dept"] == "IT":
            logging.info(f"{emp["name"]} - {emp["dept"]} - Salary: {emp["salary"]}")
        else:
            logging.warning(f"{emp["name"]} - {emp["dept"]} - Salary: {emp["salary"]}")

logging.info("Process Complete")
