import logging
import datetime

logging.basicConfig(
    filename = "time.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

today = datetime.datetime.now()
hour = today.hour
time_now = today.strftime("%H:%M:%S %p")

logging.info(f"Program started - Current time is {time_now}")


if hour < 6:
    logging.error("Its too early!")
elif hour < 12:
    logging.info("Good Morning!")
elif hour < 18:
    logging.info("Good Afternoon!")
else:
    logging.warning("Working Late!")

logging.info("Programe Complete")