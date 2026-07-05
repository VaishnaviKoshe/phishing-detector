import logging

logger = logging.getLogger("phishing_detector")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("phishing_detector.log")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)

logger.propagate = False