import logging

transactions = [
    {"id": 1, "name": "Ravi",   "type": "credit", "amount": 150000},
    {"id": 2, "name": "Sneha",  "type": "debit",  "amount": 500},
    {"id": 3, "name": "Karan",  "type": "credit", "amount": 8000},
    {"id": 4, "name": "Pooja",  "type": "debit",  "amount": 95000},
    {"id": 5, "name": "Arjun",  "type": "credit", "amount": 200},
]

logging.basicConfig(
    filename = "Transaction.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programme Started")

for emp in transactions:
    if emp['amount'] > 100000:
        logging.error(f"{emp['name']} - High Value Transaction! Amount: {emp['amount']}")
    elif emp['amount'] > 10000:
        logging.warning(f"{emp['name']} - Medium Transaction! Amount: {emp['amount']}")
    else:
        logging.info(f"{emp['name']} - Normal Transaction! Amount: {emp['amount']}")

logging.info("Programme Ended")