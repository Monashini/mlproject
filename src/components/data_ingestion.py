import os  # For handling file paths and directories
import sys  # For system-specific parameters and functions
from src.exception import CustomException  # Custom exception class (user-defined)
from src.logger import logging  # Logging module to track the flow of execution
import pandas as pd  # Pandas for data manipulation
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from dataclasses import dataclass  # To create data classes easily without writing __init__

# Data injection configuration class using dataclass
@dataclass  # This automatically generates an __init__ method
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train_csv")  # Path to save training data
    test_data_path: str = os.path.join('artifact', "test_csv")  # Path to save testing data
    raw_data_path: str = os.path.join('artifact', "data_csv")  # Path to save raw data

# Main class for data ingestion
class DataIngestion:
    def __init__(self):  
        self.ingestion_config = DataIngestionConfig()  # Create config object with paths

    def initiate_data_ingestion(self):  # Method to perform ingestion
        logging.info("entered the data ingestion method or component")  # Log start of method
        try:
            # Read the dataset from a CSV file
            df = pd.read_csv('/Users/mona/Documents/mlproject/notebook/data/StudentsPerformance.csv')  
            logging.info('read the dataset as dataframe')  # Log successful read

            # Make directory for artifacts if not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)  

            # Save the raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)  

            logging.info("Train test split initialized")  # Log split start

            # Split the data into training and testing sets
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)  

            # Save the train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)  
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)  

            logging.info("ingestion is completed")  # Log completion

            return (
                self.ingestion_config.train_data_path,  # Return path to train data
                self.ingestion_config.test_data_path    # Return path to test data
            )

        except Exception as e:  # ✅ Catching the exception properly
            #logging.error("Error occurred in data ingestion", exc_info=True)
            raise CustomException(e, sys)  # Raise custom exception with context

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
