from pandas import DataFrame


def preprocess_data(dataframe: DataFrame) -> DataFrame:
    """
    Preprocesses the given DataFrame by filling missing values with defaults,
        and casting certain columns to specific data types.

    Parameters:
    - dataframe (DataFrame): The input DataFrame containing loan application data.

    Returns:
    - DataFrame: The DataFrame with missing values handled and data types of certain columns adjusted.
    """
    dataframe.fillna({
        'Gender': 'Unknown',  # For handling missing Gender
        'Married': 'No',  # Assume not maried if missing
        'Dependents': '0',  # Assume no dependents if missing
        'Self_Employed': 'No',  # Assume not self-employed if missing
        'LoanAmount': 28,  # Assume a minimum loan is 28 if missing
        'Loan_Amount_Term': 12,  # Assume a minimum is 12 months if missing
        'Credit_History': 1,  # Assume a positive credit history if missing
        'Property_Area': 'Unknown',  # For handling missing Property_Area

    }, inplace=True)

    # Cast Credit_History to int
    dataframe['Credit_History'] = dataframe['Credit_History'].astype(int)
    # Cast CoapplicantIncome to int
    dataframe['CoapplicantIncome'] = dataframe['CoapplicantIncome'].astype(int)
    # Cast CoapplicantIncome to int
    dataframe['Dependents'] = dataframe['Dependents'].astype(str)

    return dataframe
