from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from input import * 

class InstagramBot:

    def __init__(self):
        self.username = USERNAME
        print("Input password: ")
        self.password  = input()

    def login(self):
        mobile_emulation = {"deviceName": "Nexus 5" } 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome("./driver/chromedriver", options=chrome_options)
        self.driver.implicitly_wait(5) 
        self.driver.get("https://www.instagram.com")
        self.driver.find_element_by_xpath("//button[text()='Aceptar todas']").click()
        
        time.sleep(2)

        self.driver.find_element_by_xpath("//button[text()='Entrar']").click()
        username_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")
        password_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        time.sleep(5)

        login_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button/div')
        login_button.click()

        time.sleep(5)

        try:
            self.driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        except:
            pass

        self.driver.find_element_by_xpath("//button[text()='Cancelar']").click()

        try:
            self.driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        except:
            pass
        
        time.sleep(5)


    def upload_photo(self, photo_path):
        time.sleep(2)
        
        self.driver.find_element_by_xpath("//html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav[2]/div/div/form/input").send_keys(os.path.join(os.getcwd() + photo_path))
        self.driver.find_element_by_xpath("//button[text()='Siguiente']").click()
        self.driver.find_element_by_xpath("//button[text()='Compartir']").click()

        time.sleep(5)
