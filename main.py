from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

class instagramlogin:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')

    def login(self):
        #open instagram site
        self.driver.get('https://www.instagram.com/')
        sleep(randint(3,9))

        #find username input and enter your user
        user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.clear()
        user.send_keys(self.user)
        sleep(randint(4,8))
        user.send_keys(Keys.RETURN)

        #find password input and enter your pass
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.clear()
        password.send_keys(self.password)
        sleep(randint(1,8))
        password.send_keys(Keys.RETURN)

userget = input('Enter Your Username: ')
passget = input('Enter Your Password: ')
Login = instagramlogin(user=userget,password=passget)
Login.login()
