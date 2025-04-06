import sys  # Imports the sys module to access system-specific parameters and functions like exc_info()
import logging
# Function to create a detailed error message with file name, line number, and error description
def error_message_detail(error, error_detail: sys):  
    _, _, exc_tb = error_detail.exc_info()  # Gets the traceback object from the exception
    file_name = exc_tb.tb_frame.f_code.co_filename  # Gets the name of the file where the exception occurred
    error_message = "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)  # Formats the error message string
    )
    return error_message  # Returns the formatted detailed error message

# Custom exception class that enhances error info using the error_message_detail function
class CustomException(Exception):  
    def __init__(self, error_message, error_detail: sys):  # Constructor takes error message and sys module
        super().__init__(error_message)  # Calls the base Exception constructor
        self.error_message = error_message_detail(error_message, error_detail)  # Sets the detailed error message

    def __str__(self):  # Returns the string representation of the exception
        return self.error_message  # Returns the custom detailed error message
    
