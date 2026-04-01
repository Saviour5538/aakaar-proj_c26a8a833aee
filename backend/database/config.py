import os

# Define database connection URL
DATABASE_URL = os.environ.get('DATABASE_URL')

# Define the database configuration
DATABASE_CONFIG = {
    'username': os.environ.get('DATABASE_USERNAME'),
    'password': os.environ.get('DATABASE_PASSWORD'),
    'host': os.environ.get('DATABASE_HOST'),
    'port': os.environ.get('DATABASE_PORT'),
    'database': os.environ.get('DATABASE_NAME')
}