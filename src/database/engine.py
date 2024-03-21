from sqlalchemy import create_engine

from src.config.settings import DATABASE_URL
from src.models.sqlalchemy_models import *
from src.utils.logger import logger

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)


def create_tables() -> None:
    """
    Creates database tables based on defined SQLAlchemy models if they do not already exist.
    """
    Base.metadata.create_all(engine)
    logger.info('Tables created if not existed')
