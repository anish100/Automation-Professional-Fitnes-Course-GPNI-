import menu as menu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
time.sleep(15)
driver.get("http://bvmprojects.org/gpni/web-admin/login")

# User enter the Admin Name
user_login = driver.find_element_by_name("name")
print(user_login.is_selected())
print(user_login.is_enabled())
time.sleep(5)

# User send the keys of Name
user_login.send_keys("admin")
time.sleep(5)

# User enter the Admin Password
user_pass = driver.find_element_by_name("password")
print(user_pass.is_selected())
print(user_pass.is_enabled())
time.sleep(5)

# User send the keys of the Admin Password
user_pass.send_keys("admin@123")
time.sleep(5)

#User click on the button of the signup
user_sign = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[4]/button").click()

# Open Admin profile
#User_profile = driver.find_elements_by_xpath()

# Open User Profile
#user_user_open = driver.get("http://bvmprojects.org/gpni/web-admin/manage-users");


#user_search_result = driver.find_element_by_css_selector('#simpletable_filter > label > input').send_keys(Keys.HOME,'maxwel')
#print(user_search_result)
#time.sleep(5)
# user_checkbox = driver.find_element_by_id("user_40_active")
# user_checkbox.click()
# time.sleep(5)
# user_checkbox_select = driver.find_element_by_xpath("/html/body/div[5]/div[7]/div/button").click()
# # Open the Staff Section

# #user_staff = driver.get()