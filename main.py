# Main file calling all the responsible functions into the logic
# v0.0.0.1

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from functions.logIn import logIn

def main():
    # Define main variables
    driver = webdriver.Chrome()
    # size of the screen needs to be defined eventually later removed at all
    exit = False

    # Define main bot logic
    logIn(driver)
    while(exit == False):
        action = input("What action you'd like to perform?\n")
        if(action == "exit"):
            return 0
        elif(action == "train"):
            # Here paste the training action
            return 0 # temporary
        elif(action == "fight"):
            # Here paste the fighting action
            return 0 # temporary
        elif(action == "expedition"):
            # Here paste the expedition action
            return 0 # temporary
        

if __name__ == "__main__":
    main()