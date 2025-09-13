import os
import sys

def error_message_detail(error, error_detail: sys):

    '''
    error: Exception object
    error_detail: object of sys module
    return: string message

    Function to get the details of the error like file name, line number and error message from the line where exception occurred.
    '''
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script: [{0}] at line number: [{1}] error message: [{2}]".format(
        file_name, line_number, str(error))
    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message