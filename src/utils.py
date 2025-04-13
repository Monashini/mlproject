import os
import sys
import dill
import logging
from src.exception import CustomException

# Set up logging
logger = logging.getLogger(__name__)

def save_object(obj, file_path):
    try:
        # Ensure the directory exists
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)

        # Log before saving
        logger.info(f"Saving object to {file_path}")

        # Open the file and save the object using dill
        with open(file_path, "wb") as f:
            dill.dump(obj, f)
        
        # Log after saving
        logger.info(f"Object saved successfully at {file_path}")
    
    except Exception as e:
        # Log error
        logger.error(f"Error occurred while saving object: {e}")
        raise CustomException(e, sys)
