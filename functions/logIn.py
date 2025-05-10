# This part is responsible to log in into the website
# v0.0.0.1
import getpass
import time # temporary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def logIn(driver):

    # Create variables
    userEmail = input("Enter your email: \n")
    userPassword = getpass.getpass("Enter your password: \n")
    loginUrl = "https://mistwood.pl"
    loginButtonText = "Zaloguj"
    secondLogInButtonXpath = '//*[@id="root"]/main/div/div[3]/section/form/button'
    emailEntryId = "email"
    passwordEntryId = "password"


    driver.get(loginUrl)
    logInButtonWait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, loginButtonText)))
    logInButtonWait.click()
    emailEntryFieldWait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, emailEntryId)))
    emailEntryFieldWait.send_keys(userEmail)
    passwordEntryFieldWait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, passwordEntryId)))
    passwordEntryFieldWait.send_keys(userPassword)
    secondLogInButton = driver.find_element(By.XPATH, secondLogInButtonXpath)
    secondLogInButton.click()
    
    return("Logged In!\n")
