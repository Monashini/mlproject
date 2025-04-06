import logging  # Allows logging events
import os  # Handles file paths
from datetime import datetime  # For time-stamped log files

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Unique log file name based on current time
logs_path = os.path.join(os.getcwd(), "logs")  # Directory path to store log file
os.makedirs(logs_path, exist_ok=True)  # Create 'logs' folder if not exists

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Full path to the log file

logging.basicConfig(
    filename=LOG_FILE_PATH, #Specifies the log file to write to
    format='[%(asctime)s] [line:%(lineno)d] [%(name)s] [%(levelname)s] - %(message)s',# # Defines log format
    level=logging.INFO# Sets the logging level to INFO and above (INFO, WARNING, ERROR, etc.)


)


# Logging is used to record events during program execution

# Main purposes:
# - Debugging   → Find and fix issues
# - Monitoring  → Track what the program is doing
# - Auditing    → Know who did what and when

# Instead of using print(), use logging to categorize messages:
# - logging.debug("Detailed debugging info")        → DEBUG
# - logging.info("General info about execution")    → INFO
# - logging.warning("Something unexpected")         → WARNING
# - logging.error("An error occurred")              → ERROR
# - logging.critical("Serious error, system may fail") → CRITICAL
