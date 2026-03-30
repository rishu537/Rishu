import logging

products = [
    {"name": "Laptop",  "stock": 0},
    {"name": "Phone",   "stock": 3},
    {"name": "Tablet",  "stock": 50},
    {"name": "Earbuds", "stock": 1},
    {"name": "Monitor", "stock": 25},
]

logging.basicConfig(
    filename = "Check_stocks.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programe Started")

for stc in products:
    if stc["stock"] == 0:
        logging.error(f"{stc['name']} is out of Stock!")
    elif stc["stock"] <= 5:
        logging.warning(f"{stc['name']} is low in Stocks!")
    else:
        logging.info(f"{stc['name']} is well stocked!")

logging.info("Programme Completed")
