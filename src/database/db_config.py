# dabase/db_config.py

import os

# Database Configuration
DB_NAME = os.getenv('DB_NAME', 'strasbourg')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')