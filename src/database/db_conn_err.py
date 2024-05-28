import logging
import traceback

class DatabaseConnectionError(Exception):
    def __init__(self, message="Error in database connection", code=None, original_exception=None):
        self.message = message
        self.code = code
        self.original_exception = original_exception
        super().__init__(f"{self.code}: {self.message} | Original exception: {self.original_exception}")
        self.log_error()

    def __str__(self):
        return f"DatabaseConnectionError [{self.code}]: {self.message}"

    def log_error(self):
        logger = logging.getLogger('DatabaseConnectionError')
        stack_trace = traceback.format_exc()
        logger.error(f"Raised DatabaseConnectionError with code {self.code} and message '{self.message}'. Stack trace: {stack_trace}")

    @classmethod
    def from_sql_error(cls, sql_error):
        error_message = f"Failed to execute SQL command: {sql_error.msg}"
        error_code = sql_error.errno
        return cls(message=error_message, code=error_code, original_exception=sql_error)

    @classmethod
    def from_connection_timeout(cls):
        return cls(message="Database connection timed out", code=408)
