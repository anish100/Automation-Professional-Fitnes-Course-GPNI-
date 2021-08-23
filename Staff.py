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
staff_user_open = driver.get("http://bvmprojects.org/gpni/web-admin/staff")

# User add the new staff member
staff_add_member = driver.get("http://bvmprojects.org/gpni/web-admin/staff/add-update")
staff_first_name = driver.find_element_by_name("first_name")
staff_first_name.send_keys("Dravid")

staff_last_name = driver.find_element_by_name("last_name")
staff_last_name.send_keys("Andrew")

staff_email = driver.find_element_by_name("email")
staff_email.send_keys("dravid@example.com")

staff_role = driver.find_element_by_name("role")
drp_down = Select(staff_role)
print(drp_down)
time.sleep(5)
drp_down.select_by_visible_text("Editor")
time.sleep(5)
drp_down.select_by_visible_text("Admininstrator")

# Check all the Role Name from the Dropdown list
role_options = drp_down.options
for option in role_options:
    print(option.text)