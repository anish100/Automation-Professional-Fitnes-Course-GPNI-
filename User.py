import menu as menu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
time.sleep(5)
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

# All User
user_user_open = driver.get("http://bvmprojects.org/gpni/web-admin/manage-users");


# User Searching

user_search_result = driver.find_element_by_css_selector('#simpletable_filter > label > input').send_keys(Keys.HOME,'Elvis andrew')
print(user_search_result)
time.sleep(5)


# Create New User 

new_user_open = driver.get("http://bvmprojects.org/gpni/web-admin/add-view-user-info");
time.sleep(5)

new_user_fisrtname = driver.find_element_by_name("first_name")
new_user_fisrtname.send_keys("Marconi")
print(new_user_fisrtname)
time.sleep(5)

new_user_lastname = driver.find_element_by_name("last_name")
new_user_lastname.send_keys("andrew")
print(new_user_lastname)
time.sleep(5)

new_user_credentials = driver.find_element_by_name("credentials")
new_user_credentials.send_keys("USA")
print(new_user_credentials)  
time.sleep(5)


new_user_username = driver.find_element_by_name("user_name")
new_user_username.send_keys("marconi")
print(new_user_username)
time.sleep(5)

new_user_email = driver.find_element_by_name("email")
new_user_email.send_keys("marconi@example.com")
print(new_user_email)
time.sleep(5)

new_user_password = driver.find_element_by_name("password")
new_user_password.send_keys("Marconi@123")
print(new_user_password)
time.sleep(5)

new_user_confirm_password = driver.find_element_by_name("password_confirmation")
new_user_confirm_password.send_keys("Marconi@123")
print(new_user_confirm_password)

# new_user_select_newsletter = diver.find_element_by_name("news_letter")
# new_user_select_newsletter.click()

new_user_businessname = driver.find_element_by_name("business_name")
new_user_businessname.send_keys("Professional Fitness")
print(new_user_businessname)


new_user_business_address = driver.find_element_by_name("business_address")
new_user_business_address.send_keys("London")
print(new_user_business_address)

new_user_unite_suite = driver.find_element_by_name("unit_suit")
new_user_unite_suite.send_keys("London")
print(new_user_unite_suite)

new_user_city = driver.find_element_by_name("city")
new_user_city.send_keys("Alena")
print(new_user_city)

# How to select list form dropdown fields

new_user_country = driver.find_element_by_name("country")
drp_country_select = Select(new_user_country)
print(drp_country_select)

time.sleep(5)
drp_country_select.select_by_visible_text("Algeria")

new_user_state = driver.find_element_by_name("state")
new_user_city.send_keys("Belarus")
print(new_user_city)

new_user_zipcode = driver.find_element_by_name("zip")
new_user_zipcode.send_keys("213456")
print(new_user_zipcode)

new_user_phonenumber = driver.find_element_by_name("phone")
new_user_phonenumber.send_keys("21345674567")
print(new_user_phonenumber)

new_user_faxnumber = driver.find_element_by_name("fax")
new_user_faxnumber.send_keys("34567")
print(new_user_faxnumber)

new_user_primary_email = driver.find_element_by_name("pri_email")
new_user_primary_email.send_keys("drac@example.com")
print(new_user_primary_email)

new_user_sec_email = driver.find_element_by_name("pri_sec_email")
new_user_sec_email.send_keys("drac2@example.com")
print(new_user_sec_email)

new_user_website = driver.find_element_by_name("website")
new_user_website.send_keys("googleanish")
print(new_user_website)

# Select the list from dropdwon list

new_user_age = driver.find_element_by_name("age")
drp_new_user_age = Select(new_user_age)
drp_new_user_age.select_by_visible_text("30-39")
print(drp_new_user_age)

new_user_areainterest = driver.find_element_by_name("interest")
drp_new_user_areainterest = Select(new_user_areainterest)
drp_new_user_areainterest.select_by_visible_text("Research and Development")
print(drp_new_user_areainterest)


new_user_occupation = driver.find_element_by_name("occupation")
drp_new_user_occupation = Select(new_user_occupation)
drp_new_user_occupation.select_by_visible_text("Industry Product Development/Sales")
print(drp_new_user_occupation)


new_user_messengerapp = driver.find_element_by_name("messenger_app")
drp_new_user_messengerapp = Select(new_user_messengerapp)
drp_new_user_messengerapp.select_by_visible_text("WhatsAPP")
print(drp_new_user_messengerapp)


new_user_where_hear = driver.find_element_by_name("where_hear")
drp_new_user_where_hear = Select(new_user_where_hear)
drp_new_user_where_hear.select_by_visible_text("Social Media")
print(drp_new_user_where_hear)


new_user_hear_person_name = driver.find_element_by_name("hear_person_name")
new_user_hear_person_name.send_keys("Alena")
print(new_user_hear_person_name)


new_user_create = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div[2]/form/button").click()


new_user_create_success = driver.ind_element_by_xpath("/html/body/div[5]/div[7]/div/button").click()


driver.get("http://bvmprojects.org/gpni/web-admin/manage-users")








