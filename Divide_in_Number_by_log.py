import logging

logging.basicConfig(
    filename = "error.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a,b):
    try:
        logging.info(f"Dividing {a} by {b}")
        result = a/b
        logging.info(f"result : {result}")
        return result
    except ZeroDivisionError:
        logging.error("Cannot divide by zero")

divide(10,2)
divide(5,0)