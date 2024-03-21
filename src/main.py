import pandas as pd

from src.database.engine import *
from src.models.pydantic_models import *
from src.services.data_loader import *
from src.services.preprocess import preprocess_data
from src.utils.logger import logger


def process_csv_data(csv_path: str, data_model, data_table) -> None:
    """
    Process CSV data by reading, preprocessing, and loading it into a database.

    Parameters:
    - csv_path: Path to the CSV file.
    - data_model: The Pydantic model for data validation.
    - data_table: The SQLAlchemy model for database insertion.
    """
    df = pd.read_csv(csv_path)
    df = preprocess_data(df)  # Preprocess data before loading
    load_data_to_database(df, data_model, data_table)  # Load with validation


def main():
    """ Main module for executing the ETL process. """
    try:
        logger.info('Starting ETL process')
        create_tables()

        # Data processing configurations
        data_configs = [
            ('raw_data/loan-test.csv', TestDataModel, TestDataTable),
            ('raw_data/loan-train.csv', TrainDataModel, TrainDataTable),
        ]

        # Process each dataset
        for csv_path, data_model, data_table in data_configs:
            process_csv_data(csv_path, data_model, data_table)

        logger.info('ETL process is finished')
    except Exception as e:
        logger.error(f'Failed to complete ETL process: {e}', exc_info=True)


if __name__ == "__main__":
    main()
