import logging
import datetime

logging.basicConfig(
    filename = "season.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

today = datetime.datetime.now()
month = today.month
month_name = today.strftime("%d %B %Y")

logging.info(f"Programme Started - Current Season is {month_name}")

if month in [12, 1, 2]:
    logging.warning("Winter")
elif month in [3, 4, 5]:
    logging.info("Spring")
elif month in [6, 7, 8]:
    logging.error("Summer")
else:
    logging.info("Autumn")

logging.info("Programe Complted! ")