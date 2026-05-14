from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login(driver):

    driver.find_element(By.ID,"signin2").click()
    driver.find_element(By.ID,"sign-username").send_keys("username")
    driver.find_element(By.ID,"sign-password").send_keys("password")
    driver.find_element(By.XPATH,"//button[text()='Sign up']").click()

