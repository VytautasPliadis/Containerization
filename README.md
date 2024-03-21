![LOAN.png](img%2FLOAN.png)
# Containerization
The project is focused on creating a data pipeline for machine learning models, which is outside the scope of this 
project, to predict customer creditworthiness. It involves automating the collection, processing, and storage of
loan-related data to support informed decision-making. The solution is containerized using Docker to facilitate easy 
deployment on any system with Docker installed, aiming to simplify the integration of data engineering and predictive 
analytics in the credit assessment process.


## Features

- **Data Processing**: Customizable data loading and preprocessing modules (`data_loader.py`, `preprocess.py`) to efficiently handle and prepare data for analysis or further processing.
- **Logging**: `logger.py` provides detailed insights into the application's runtime behavior, aiding in debugging and monitoring.
- **Database Integration**: Seamless integration with databases using SQLAlchemy models (`sqlalchemy_models.py`), allowing for efficient data storage, retrieval, and manipulation.
- **Configuration Management**: Easy-to-manage application settings (`settings.py`) that support dynamic configuration to adapt to different environments or deployment needs.
- **Pydantic Models**: Use of Pydantic models (`pydantic_models.py`) for data validation and schema definition, enhancing data integrity and error handling.
- **Docker Support**: Full Docker integration with a `Dockerfile` and `docker-compose.yml`, enabling straightforward deployment, scaling, and versioning in any environment.
- **Main Application Logic**: The `main.py` module serves as the entry point to the application.


## Prerequisites

Before running `docker-compose.yml`, ensure you have necessary environment variables listed in the `.env` file 
(or configure them directly in the `docker-compose.yml`).
Download dataset to the mount volume using `download_data.py`.

## Data Assumptions

The project incorporates several key assumptions regarding data handling, particularly in the context of missing values:

- **Gender**: When Gender values are missing, 'Unknown' is assumed. This strategy ensures data handling is neutral and inclusive.

- **Married**: The absence of an applicant's marital status leads to the assumption of 'No', suggesting they are not married.
This presumption is based on the probability that married individuals would disclose their marital status, 
considering its significance in financial evaluations.

- **Dependents**: Should data on dependents be missing, '0' is assumed. This cautious approach aims to avoid overestimating 
an applicant's financial obligations, which is vital for evaluating their capacity to repay a loan.

- **Self_Employed**: A lack of information regarding self-employment results in the assumption of 'No', indicating 
a bias towards traditional employment.

- **LoanAmount**: Absent loan amount values are set to 28 (reflecting the dataset's context).

- **Loan_Amount_Term**: Missing values for the loan term are assumed to be a minimum of 12 months. This presumption is 
in line with the lending institution's offerings (dataset's context), suggesting that all loans are expected to have at
least a one-year repayment period.

- **Credit_History**: In the event of missing credit history information, a positive credit history ('1') is assumed, 
optimistically indicating the applicant's creditworthiness. Although this might introduce a positive bias in the loan 
approval process, it represents a conscious decision to presume eligibility in the absence of explicit data.

- **Property_Area**: Unspecified property area details are labeled as 'Unknown', avoiding unfounded conjectures about
an applicant's place of residence or property location. This impartial stance is essential to prevent geographical 
biases in the loan decision-making process.

It is important for these assumptions to be validated against known data patterns or external information whenever possible,
to ensure alignment with real-world conditions.

## Project Structure
```   
containerization/
├─── Dockerfile
├─── .dockerignore
├─── docker-compose.yml
├─── requirements.txt
├─── pyproject.toml
├─── README.md
├─── .env
│
├── src/
│   ├── __init__.py
│   ├── download_data.py ..............download data to the mount volume.
│   ├── main.py .......................main module for executing the etl process.
│   ├── models/
│   │   ├── __init__.py
│   │   ├── sqlalchemy_models.py ......sqlalchemy orm models.
│   │   └── pydantic_models.py ........pydantic models for data validation.
│   ├── database/
│   │   ├── __init__.py
│   │   └── engine.py .................sqlalchemy engine for database interactions.   
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py ...............environment variables.
│   ├── services/
│   │   ├── __init__.py
│   │   ├── data_preprocessing.py .....preprocessing (cleaning) data. 
│   │   ├── data_loader.py ............validates and inserts data into a database.
│   │   └── downloader.py .............downloads a dataset.
│   └── utils/
│       ├── __init__.py
│       └── logger.py .................logging configuration.
├── raw_data/
│   ├── loan-test.csv 
│   └── loan-train.csv
└── img/
    └── loan.png

```
