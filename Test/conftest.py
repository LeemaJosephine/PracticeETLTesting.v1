import pytest
import pymysql


@pytest.fixture
def db_connection():

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="employee_db"
    )

    yield connection

    connection.close()