import pytest
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
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