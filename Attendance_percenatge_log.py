import logging

students = [
    {"name": "Aman",   "attendance": 95},
    {"name": "Sneha",  "attendance": 72},
    {"name": "Rohan",  "attendance": 45},
    {"name": "Priya",  "attendance": 60},
    {"name": "Anjali", "attendance": 30},
]

logging.basicConfig(
    filename = "percentage.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programme Started")

for stu in students:
    if stu['attendance'] > 75:
        logging.info(f"{stu['name']} has Excellent Attendance")
    elif stu['attendance'] >= 50:
        logging.warning(f"{stu['name']} attendance is average")
    else:
        logging.error(f"{stu['name']} Attendance is critical")

logging.info("Programme Ended")