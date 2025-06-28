from dotenv import load_dotenv
import logging
import os

load_dotenv()

# Get log level and log file from environment variables
log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
log_level = getattr(logging, log_level_str, logging.INFO)
LOG_FILE = os.getenv("LOG_FILE", "calculator.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=log_level,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

