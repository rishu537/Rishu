import logging
import datetime

orders = [
    {"order_id": 1, "product": "Laptop",  "amount": 75000, "status": "delivered"},
    {"order_id": 2, "product": "Phone",   "amount": 15000, "status": "pending"},
    {"order_id": 3, "product": "Tablet",  "amount": 25000, "status": "cancelled"},
    {"order_id": 4, "product": "Monitor", "amount": 12000, "status": "delivered"},
    {"order_id": 5, "product": "Mouse",   "amount": 999,   "status": "pending"},
]

logging.basicConfig(
    filename = "pipeline.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

today = datetime.datetime.now()
date_now = today.strftime("%d-%m-%Y %H:%M:%S")

logging.info(f"PipeLine Started at {date_now}")
logging.info(f"Total Order found: {len(orders)}")

for order in orders:
    if order['status'] == "delivered":
        logging.info(f"Order {order['order_id']} - {order['product']} {order['status']}")
    elif order['status'] == "pending":
        logging.warning(f"Order {order['order_id']} - {order['product']} {order['status']}")
    else:
        logging.error(f"Order {order['order_id']} - {order['product']} {order['status']}")

logging.info("Programme Completed")