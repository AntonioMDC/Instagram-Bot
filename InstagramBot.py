from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import configparser



class InstagramBot:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("account_info.ini")
        self.username = config['DEFAULT']["account_name"]
        print("Input password: ")
        self.password  = input()

    def login(self):
        mobile_emulation = {"deviceName": "Nexus 5" } 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome("./driver/chromedriver", options=chrome_options)
        driver.implicitly_wait(5) 
        driver.get("https://www.instagram.com")
        driver.find_element_by_xpath("//button[text()='Aceptar todas']").click()
        
        time.sleep(2)

        driver.find_element_by_xpath("//button[text()='Entrar']").click()
        username_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input")
        password_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)

        time.sleep(5)

        login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button/div')
        login_button.click()

        time.sleep(5)

        driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        driver.find_element_by_xpath("//button[text()='Cancelar']").click()
        driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        time.sleep(5)

