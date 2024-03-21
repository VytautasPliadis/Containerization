from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CommonColumns(Base):
    __abstract__ = True
    Loan_ID = Column(String, primary_key=True)
    Gender = Column(String)
    Married = Column(String)
    Dependents = Column(String)
    Education = Column(String)
    Self_Employed = Column(String)
    ApplicantIncome = Column(Integer)
    CoapplicantIncome = Column(Integer)
    LoanAmount = Column(Float)
    Loan_Amount_Term = Column(Integer)
    Credit_History = Column(Boolean)
    Property_Area = Column(String)


class TestDataTable(CommonColumns):
    """
    Defines the schema for the test data table, inheriting common columns from CommonColumns.
    This class is used to create and manipulate the test dataset in the database.
    """
    __tablename__ = 'test_data'


class TrainDataTable(CommonColumns):
    """
    Defines the schema for the training data table, extending CommonColumns with a Loan_Status column.
    """
    __tablename__ = 'train_data'
    Loan_Status = Column(String)
