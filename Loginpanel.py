import menu as menu
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
time.sleep(15)
driver.get("http://bvmprojects.org/gpni/")

new_register = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/a[1]").click()
print(new_register)

new_user_fisrtname = driver.find_element_by_name("first_name")
new_user_fisrtname.send_keys("Decade")
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
new_user_username.send_keys("decade")
print(new_user_username)
time.sleep(5)

new_user_email = driver.find_element_by_name("email")
new_user_email.send_keys("decade@example.com")
print(new_user_email)
time.sleep(5)

new_user_confirm_email = driver.find_element_by_id("confirm_email")
new_user_confirm_email.send_keys("decade@example.com")
print(new_user_confirm_email)
time.sleep(5)


new_user_password = driver.find_element_by_name("password")
new_user_password.send_keys("Decade@123")
print(new_user_password)
time.sleep(5)

new_user_confirm_password = driver.find_element_by_name("password_confirmation")
new_user_confirm_password.send_keys("Decade@123")
print(new_user_confirm_password)

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
new_user_primary_email.send_keys("decade@example.com")
print(new_user_primary_email)

new_user_sec_email = driver.find_element_by_name("pri_sec_email")
new_user_sec_email.send_keys("decade2@example.com")
print(new_user_sec_email)

new_user_website = driver.find_element_by_name("website")
new_user_website.send_keys("googledecade")
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

register_submit_button = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/form/button").click()
print(register_submit_button)


driver.get("http://bvmprojects.org/gpni/login")
#decade@example.com
#Decade@123

user_login_email = driver.find_element_by_name("email")
user_login_email.send_keys("decade@example.com")

user_login_password = driver.find_element_by_name("password")
user_login_password.send_keys("Decade@123")

user_login_button_click = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div/form/button").click()

# User are open Dashboard
user_dashboard_open = driver.get("http://bvmprojects.org/gpni/dashboard")
print(user_dashboard_open)


#Scrolling Down of the page
driver.execute_script("window.scrollTo(0, window.scrollY + 2000)")
time.sleep(5)

# Scrolling up of the page

driver.execute_script("window.scrollTo(0, window.scrollY + 0)")
time.sleep(5)


# Course are displayed.
user_dash_course = driver.get("http://bvmprojects.org/gpni/user-courses")
print(user_dash_course)
time.sleep(3)

# Payment Transaction
user_dash_payment = driver.get("http://bvmprojects.org/gpni/dashboard/user-transactions")
print(user_dash_payment)
time.sleep(3)

# Membership plan
user_dash_membership = driver.get("http://bvmprojects.org/gpni/dashboard/membership-plan-info")
print(user_dash_membership)
time.sleep(3)


# User able to view Mystorage
user_dash_mystorage = driver.get("http://bvmprojects.org/gpni/dashboard/my-storage")
print(user_dash_mystorage)
time.sleep(3)

user_mystorage_image = driver.get("http://bvmprojects.org/gpni/dashboard/my-storage/image")
print(user_mystorage_image)
time.sleep(3)


user_mystorage_video = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/ul/li[3]/a").click()
print(user_mystorage_video)
time.sleep(3)

user_mystorage_pdf = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/ul/li[4]/a").click()
print(user_mystorage_pdf)
time.sleep(3)


user_mystorage_ppt = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/ul/li[5]/a").click()
print(user_mystorage_ppt)
time.sleep(3)


user_mystorage_excel = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/ul/li[5]/a").click()
print(user_mystorage_excel)
time.sleep(3)


user_mystorage_doc = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/ul/li[7]/a").click()
print(user_mystorage_doc)
time.sleep(3)


user_mystorage_audio = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/ul/li[8]/a").click()
print(user_mystorage_audio)
time.sleep(3)



user_mystorage_newadd = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div[1]/a").click()
print(user_mystorage_newadd)
time.sleep(3)


user_mystorage_newadd_type = driver.find_element_by_name("type")
drp_user_mystorage_newadd_type = Select(user_mystorage_newadd_type)
drp_user_mystorage_newadd_type.select_by_visible_text("Image")
time.sleep(3)


user_mystorage_newadd_name = driver.find_element_by_name("name")
user_mystorage_newadd_name.send_keys("Fitness Image")

# user_mystorage_newadd_imageupload = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/form/div[3]/div/input")
# user_mystorage_newadd_imageupload.send_keys("C:\\Users\\dell\\Desktop\\GPNI\\images (13).jpg")
# user_mystorage_newadd_image_submit = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/form/button").click()

# User able to view order

user_dash_order = driver.get("http://bvmprojects.org/gpni/dashboard/my-orders")
print(user_dash_order)
#user_dash_order_view = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[5]/a").click()

user_dash_askaquestion = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[2]/ul/li[7]/a").click()

user_dash_askaquestion_title = driver.find_element_by_name("title")
user_dash_askaquestion_title.send_keys("Professional Fitness")

user_dash_askaquestion_comment = driver.find_element_by_name("comment")
user_dash_askaquestion_comment.send_keys("I am Professional trainer")
user_dash_askaquestion_comment_submit = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div/div/div[1]/form/button").click()
time.sleep(3)

user_dash_askaquestion_reply = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div/ul/li[2]/a").click()


# user able to view all the Points

user_dash_points = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[2]/ul/li[8]/a").click()
print(user_dash_points)

user_dash_cec_points = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[2]/ul/li[8]/a").click()
print(user_dash_cec_points)

# User are open the Referral section
user_dash_referral = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[2]/ul/li[10]/a").click()
time.sleep(4)
user_dash_referral_refer = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/a").click()
user_dash_referral_refer_email = driver.find_element_by_name("email")
user_dash_referral_refer_email.send_keys("monty@example.com")
user_dash_referral_refer_email_submit = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div/div/div/div/form/button").click()


#User are open to withdraw request

user_dash_withdraw = driver.find_element_by_xpath("/html/body/section/div/div/div[1]/div[2]/ul/li[11]/a").click()
print(user_dash_withdraw)

# user_dash_withdraw_request = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/a").click()
# user_dash_withdraw_amount = driver.find_element_by_name("redeem_amount")
# user_dash_withdraw_amount.send_keys("204")

# user_dash_withdraw_submit = driver.find_element_by_xpath("/html/body/section/div/div/div[2]/div/div[2]/div/div/div/form/button").click()


#User are open Subsribe Membership

user_sub_member_open = driver.get("http://bvmprojects.org/gpni/membership-subscription")
print(user_sub_member_open)
user_sub_member_paidplan = driver.find_element_by_xpath("/html/body/section/div/div[2]/div/div[2]/a").click()

user_sub_member_credit = driver.find_element_by_xpath("/html/body/section/div/div/div/div[3]/form/button").click()
user_sub_member_cardnumber = driver.find_element_by_xpath("/html/body/section/div/div/div/form/div[1]/div/input")
user_sub_member_cardnumber.send_keys("4242424242424242")
user_sub_member_expmonth = driver.find_element_by_xpath("/html/body/section/div/div/div/form/div[2]/div[1]/input")
user_sub_member_expmonth.send_keys("02")
user_sub_member_years = driver.find_element_by_xpath("/html/body/section/div/div/div/form/div[2]/div[2]/input")
user_sub_member_years.send_keys("2025")

user_sub_member_cbcnumber = driver.find_element_by_xpath("/html/body/section/div/div/div/form/div[2]/div[3]/input")
user_sub_member_cbcnumber.send_keys("345")

user_sub_member_submit = driver.find_element_by_xpath("/html/body/section/div/div/div/form/div[4]/div/button").click()

#User are open Membershib Contents

user_member_content_open = driver.get("http://bvmprojects.org/gpni/members-access/access-denied")
user_member_content_click = driver.find_element_by_xpath("/html/body/section/div/div[3]/div/div/a").click()


#User able to view About Us page

user_about = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/a").click()
user_about_historygpni = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/ul/li[1]/a").click()
time.sleep(3)
user_about = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/a").click()
user_about_issnpartner = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/ul/li[2]/a").click()
time.sleep(3)
user_about = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/a").click()
user_about_fundingteam = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/ul/li[3]/a").click()
time.sleep(3)
user_about = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/a").click()
user_about_fundingteam = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[1]/ul/li[4]/a").click()
time.sleep(3)
# Professional Education

user_professional_open = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[2]/a").click()
time.sleep(3)
user_certification_dip = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[2]/ul/li[1]/a").click()
time.sleep(3)

user_professional_open = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[2]/a").click()
time.sleep(3)
user_cec_certification = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[2]/ul/li[2]/a").click()
time.sleep(3)

user_professional_open = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[2]/a").click()
time.sleep(3)
user_mini_course = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[2]/ul/li[2]/a").click()
time.sleep(3)


user_programs = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[3]/a").click()
drp_programs = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[3]/ul/li/a").click()
time.sleep(4)

user_resources_articles = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/a").click()
drp_all_articles = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/ul/li[1]/a").click()
time.sleep(4)

user_resources_articles = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/a").click()
drp_fitness = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/ul/li[2]/a").click()
time.sleep(4)

user_resources_articles = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/a").click()
drp_profitness = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/ul/li[3]/a").click()
time.sleep(4)


user_resources_articles = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/a").click()
drp_scie_research = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/ul/li[4]/a").click()
time.sleep(4)

user_resources_articles = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/a").click()
drp_social = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[4]/ul/li[5]/a").click()
time.sleep(4)


user_qualified_coaches = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[5]/a").click()
drp_cerfied_coaches = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[5]/ul/li/a").click()

user_product = driver.find_element_by_xpath("/html/body/header/nav/div/div/ul/li[6]/a").click()
print(user_product)

user_product_books = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[2]/a").click()
time.sleep(3)
user_product_guides = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[3]/a").click()
time.sleep(3)

user_product_merchandise = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[4]/a").click()
time.sleep(3)

user_product_clothing = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[5]/a").click()
time.sleep(3)

user_product_course = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[6]/a").click()
time.sleep(3)

user_product_conference = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[7]/a").click()
time.sleep(3)

user_product_online = driver.find_element_by_xpath("/html/body/section[2]/div/div/ul/li[8]/a").click()
time.sleep(3)



#User open all the link from Footer of the Page.

#ABOUT Us

history_page = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[1]/div/ul/li[1]/a").click()
time.sleep(3)

issn_partner = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[1]/div/ul/li[2]/a").click()
time.sleep(3)

founding_team = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[1]/div/ul/li[3]/a").click()
time.sleep(3)

Advisory_board = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[1]/div/ul/li[4]/a").click()
time.sleep(3)

privacy_policy = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[1]/div/ul/li[5]/a").click()
time.sleep(2)

# Education

certif_diploma = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[2]/div/ul/li[1]/a").click()
time.sleep(2)

education_credit = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[2]/div/ul/li[2]/a").click()
time.sleep(2)

mini_courses = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[2]/div/ul/li[3]/a").click()
time.sleep(2)

# Resources and Articles

all_articles = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[3]/div/ul/ul/li[1]/a").click()
time.sleep(2)

fitness  = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[3]/div/ul/ul/li[2]/a").click()
time.sleep(2)

professional_fitness = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[3]/div/ul/ul/li[3]/a").click()
time.sleep(2)

scientific_research = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[3]/div/ul/ul/li[4]/a").click()
time.sleep(2)

social_media = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[3]/div/ul/ul/li[5]/a").click()
time.sleep(2)


footer_email_enter = driver.find_element_by_xpath("/html/body/footer/div[1]/div/div/div[5]/div[1]/form/input[1]")
footer_email_enter.send_keys("mark@example.com")





































