import logging
import datetime

logging.basicConfig(
    filename = "day.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

today = datetime.datetime.now()
day_name = today.strftime("%a")

logging.info(f"Program Started - Today is {day_name}")

if day_name in ["Saturday", "Sunday"]:
    logging.error(f"{day_name} is a Weekend")
elif day_name == "Monday":
    logging.warning(f"{day_name} - Start of the week!")
else:
    logging.info(f"{day_name} - Normal Working Day")

logging.info("Program completed")