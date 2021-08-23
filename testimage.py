import menu as menu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
time.sleep(15)
driver.get("http://bvmprojects.org/gpni/login")
#decade@example.com
#Decade@123

user_login_email = driver.find_element_by_name("email")
user_login_email.send_keys("decade@example.com")

user_login_password = driver.find_element_by_name("password")
user_login_password.send_keys("Decade@123")

# user_login_button_click = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/form/button").click()

# # User are open Dashboard
# user_dashboard_open = driver.get("http://bvmprojects.org/gpni/dashboard")
# print(user_dashboard_open)

# user_image_click = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[1]/div/div[1]/a/i").click()
# print(user_image_click)

# user_image_select = driver.find_element_by_xpath("/html/body").click()
# print(user_image_select)



# #Affiliate syatem of the gpni

# user_affiliate = driver.find_element_by_xpath("")