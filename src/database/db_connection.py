import mysql.connector
from mysql.connector import Error, pooling
from . import db_config, db_conn_err
from utils.setup_logging import setup_logger
import time

# Configure logging to database.log
logger = setup_logger('database', log_file='database.log')

class DatabaseConnection:
    def __init__(self):
        self.config = {
            "database": db_config.DB_NAME,
            "user": db_config.DB_USER,
            "password": db_config.DB_PASSWORD,
            "host": db_config.DB_HOST,
            "use_pure": True,
            "ssl_disabled": False,
        }
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_size=10, **self.config)
    
    def get_connection(self):
        return self.pool.get_connection()

    def __enter__(self):
        self.connection = self.get_connection()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("Database connection closed")

    def execute_query(self, query, data=None, commit=True):
        if not self.connection or not self.connection.is_connected():
            self.connection = self.get_connection()
        start_time = time.time()
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, data)
                if cursor.with_rows:
                    results = cursor.fetchall()
                    if commit:
                        self.connection.commit()
                    logger.info(f"Query executed in {time.time() - start_time:.2f} seconds: {query}")
                    return results
                else:
                    if commit:
                        self.connection.commit()
                    logger.info(f"Query executed successfully: {query}")
        except Error as e:
            self.connection.rollback()
            logger.error(f"Error executing query: {e}")
            raise db_conn_err.DatabaseConnectionError(f"Error executing query: {e}")

    def fetch_query_results(self, query, data=None):
        return self.execute_query(query, data, commit=False)
