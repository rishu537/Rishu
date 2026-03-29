import logging

logging.basicConfig(
    filename="Student.log",
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Programme Started")
logging.debug("Loading data..")
logging.info("Data Loaded Successfull")
logging.warning("Memory low")
logging.error("File not found")
