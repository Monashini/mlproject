import os  # For handling file paths and directories
import sys  # For system-specific parameters and functions

# Add the project root to sys.path so that imports of "src" work correctly.
# This hack adds the directory two levels up from the current file's directory.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from src.exception import CustomException  # Custom exception class (user-defined)
from src.logger import logging           # Logging module to track the flow of execution
import pandas as pd                      # Pandas for data manipulation
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from dataclasses import dataclass         # To create data classes easily without writing __init__

# Import the DataTransformation class from data_transformation.py
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationconfig

# Data ingestion configuration class using dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")  # Path to save training data
    test_data_path: str = os.path.join('artifact', "test.csv")    # Path to save testing data
    raw_data_path: str = os.path.join('artifact', "data.csv")      # Path to save raw data

# Main class for data ingestion
class DataIngestion:
    def __init__(self):  
        self.ingestion_config = DataIngestionConfig()  # Create config object with paths

    def initiate_data_ingestion(self):  # Method to perform ingestion
        logging.info("Entered the data ingestion method/component")
        try:
            # Read the dataset from a CSV file
            df = pd.read_csv('/Users/mona/Documents/mlproject/notebook/data/StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            # Create directory for artifacts if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-test split initialized")

            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion is completed")

            return (
                self.ingestion_config.train_data_path,  # Return path to train data
                self.ingestion_config.test_data_path    # Return path to test data
            )

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    # Run the data ingestion process
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # Run the data transformation process
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
