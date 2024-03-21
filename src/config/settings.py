import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
TEST_CSV_PATH = os.getenv('TEST_CSV_PATH')
TRAIN_CSV_PATH = os.getenv('TRAIN_CSV_PATH')

# Load kaggle variables
KAGGLE_USERNAME = os.getenv('KAGGLE_USERNAME')
KAGGLE_KEY = os.getenv('KAGGLE_KEY')
dataset_id = os.getenv('dataset_id')