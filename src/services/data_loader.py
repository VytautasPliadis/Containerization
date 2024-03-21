from typing import Type, Optional

from pandas import DataFrame
from pydantic import BaseModel, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.database.engine import engine
from src.utils.logger import logger


def load_data_to_database(dataframe: DataFrame, model: Type[BaseModel],
                          sqlalchemy_model: Type[declarative_base()],
                          batch_size: int = 1000,
                          identifier_column: Optional[str] = None) -> None:
    """
    Validates and inserts data into a database with error handling and batch processing.

    Parameters:
    - dataframe: The DataFrame containing the data to be inserted.
    - model: The Pydantic model class used for data validation.
    - sqlalchemy_model: The SQLAlchemy model class used for data insertion.
    - batch_size: The number of records to process in each batch.
    - identifier_column: The name of the column to use as a row identifier in logs.
    """
    Session = sessionmaker(bind=engine)
    total_inserted = 0
    errors = []

    with Session() as session:
        for start_row in range(0, dataframe.shape[0], batch_size):
            data_to_insert = []  # List to collect validated rows for the current batch
            batch_errors = []

            for _, row in dataframe.iloc[start_row:start_row + batch_size].iterrows():
                try:
                    validated_data = model(**row.to_dict())
                    # Convert directly to the SQLAlchemy model instance
                    sqlalchemy_instance = sqlalchemy_model(**validated_data.dict())
                    data_to_insert.append(sqlalchemy_instance)
                except ValidationError as e:
                    error_msg = f"Validation error for row {row.get(identifier_column, 'unknown')}: {e}"
                    batch_errors.append(error_msg)

            if data_to_insert:
                try:
                    session.add_all(data_to_insert)
                    session.commit()
                    total_inserted += len(data_to_insert)
                    logger.info(f"Bulk inserted {len(data_to_insert)} records into {sqlalchemy_model.__tablename__}.")
                except SQLAlchemyError as e:
                    logger.error(f"Transaction failed, rolling back. Error: {e}")
                    session.rollback()
                    batch_errors.append(f"SQLAlchemy Error: {e}")

            errors.extend(batch_errors)

    if errors:
        logger.error(f"Completed with errors. Total inserted: {total_inserted}, Errors: {len(errors)}")
        for error in errors:
            logger.error(error)
    else:
        logger.info(f"Successfully inserted {total_inserted} records without any errors.")
