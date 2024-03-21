from typing import Literal
from pydantic import BaseModel


class TestDataModel(BaseModel):
    """
    A Pydantic model representing the schema for validating test data in the loan application process.
    """
    Loan_ID: str
    Gender: Literal['Male', 'Female', 'Unknown']
    Married: Literal['Yes', 'No']
    Dependents: Literal['0', '1', '2', '3+']
    Education: Literal['Graduate', 'Not Graduate']
    Self_Employed: Literal['Yes', 'No']
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: Literal[0, 1]
    Property_Area: Literal['Rural', 'Semiurban', 'Urban', 'Unknown']


class TrainDataModel(TestDataModel):
    """
    A Pydantic model extending TestDataModel. This model adds a field for the loan status.
    """
    Loan_Status: Literal['Y', 'N']
