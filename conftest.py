import pytest
import pymysql
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(20)

    yield driver



    #driver.quit()


    # connection = pymysql.connect(
    #     host="localhost",
    #     user="root",
    #     password="root",
    #     database="employee_db"
    # )
    #
    # yield connection
    #
    # connection.close()