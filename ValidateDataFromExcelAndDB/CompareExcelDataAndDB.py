import pandas as pd
import pymysql
import pytest

from Test.conftest import db_connection


def test_data_validation(db_connection):
    # Read data from Excel
    excel_data=pd.read_excel("C:\\Users\\leema\\PycharmProjects\\PracticeETLTesting\\Data\\Test_Data.xlsx")

    # Reda data from DB

    cursor = db_connection.cursor()

    # Read and fetch data

    query ="Select * from salary_info"
    cursor.execute(query)
    data_db = cursor.fetchall()

    # Convert DB data to DataFormat

    db_df = pd.DataFrame(
        data_db,
        columns=["emp_id", "emp_name", "salary"]
    )

    print(db_df)
    print(excel_data)

    # Standardize columns
    excel_data.columns = excel_data.columns.str.lower().str.strip()
    db_df.columns = db_df.columns.str.lower().str.strip()

    # Compare
    assert excel_data.equals(db_df), "Excel and DB data are NOT matching"

    print("Data Validation Successful")