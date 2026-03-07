from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

# Qestion-1
# Write a script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Books
# Add first book to cart
# Click Shopping Cart
# Verify the product is present in the cart.


# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element('xpath','(//a[contains(text(),"Book")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath','(//input[@value="Add to cart"])[1]').click()
# time.sleep(2)
# product = driver.find_element('xpath','(//span[@class="cart-label"])[1]')
# if product:
#     print("Product present in cart:", product)





#Question-2
# Write a Selenium script to:
# Open https://www.demowebshop.tricentis.com
# Navigate to Electronics
# Use XPath contains() to locate the Cell Phones category
# Click it.

# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element('xpath','//a[contains(text(),"Electronics")]').click()
# time.sleep(5)
# driver.find_element('xpath','(//a[contains(text(),"Cell phones")])[1]').click()





#Question-3
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.


# driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
# driver.find_element('xpath','//button[text()="Start"]').click()
# time.sleep(5)
# text = driver.find_element('xpath','//h4[text()="Hello World!"]').text
# print(text)







#Question-4
# Write a script to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add

# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# driver.find_element('xpath','//button[text()="Remove"]').click()
# time.sleep(5)
# driver.find_element('xpath','//button[text()="Add"]').click()







# Question-5
# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.


# driver.get("https://demoqa.com/select-menu")
# time.sleep(3)
#
# driver.find_element('xpath','//div[@id="withOptGroup"]').click()
# time.sleep(2)
# driver.find_element('xpath','//div[text()="Group 2, option 1"]').click()
# time.sleep(2)
# value = driver.find_element('xpath','//div[@id="withOptGroup"]').text
# print("Selected value:", value)







#Question-6
# Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.


# driver.get("https://demoqa.com/select-menu")
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,600)")
# time.sleep(2)
# multi_select = Select(driver.find_element('xpath','//select[@id="cars"]'))
# multi_select.select_by_visible_text("Volvo")
# multi_select.select_by_visible_text("Saab")
# multi_select.select_by_visible_text("Opel")
# time.sleep(2)
# selected_options = multi_select.all_selected_options
# for option in selected_options:
#     print(option.text)






#Question-7
# Write a Selenium script to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1



# driver.get("https://demoqa.com/menu/")
# time.sleep(3)
#
# actions = ActionChains(driver)
# main_item = driver.find_element('xpath','//a[text()="Main Item 2"]')
# actions.move_to_element(main_item).perform()
# time.sleep(2)
#
# sub_sub_list = driver.find_element('xpath','//a[text()="SUB SUB LIST »"]')
# actions.move_to_element(sub_sub_list).perform()
# time.sleep(2)
#
# driver.find_element('xpath','//a[text()="Sub Sub Item 1"]').click()
# time.sleep(2)






#Question-8
# Write a Selenium script to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!


# driver.get("https://demoqa.com/droppable")
# time.sleep(3)
#
# actions = ActionChains(driver)
#
# drag_item = driver.find_element('xpath','//div[@id="draggable"]')
# drop_item = driver.find_element('xpath','//div[@id="droppable"]')
#
# actions.drag_and_drop(drag_item, drop_item).perform()
# time.sleep(2)
#
# text = driver.find_element('xpath','//div[@id="droppable"]').text
#
# print("Drop result:", text)






#Question-9
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/javascript_alerts
# Click JS Confirm
# Accept the alert
# Verify result text shows You clicked: Ok


# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Click for JS Confirm"]').click()
# time.sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2)
#
# result = driver.find_element('xpath','//p[@id="result"]').text
# print("Result:", result)





# Question-10
# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/upload
# Upload a file from local system
# Click Upload
# Verify uploaded file name


# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
#
# file_path = r"C:\Users\KIIT\Desktop\Training_Exam\req.txt"
# driver.find_element('xpath','//input[@id="file-upload"]').send_keys(file_path)
# time.sleep(2)
#
# driver.find_element('xpath','//input[@id="file-submit"]').click()
# time.sleep(2)
#
# uploaded_file = driver.find_element('xpath','//div[@id="uploaded-files"]').text
# print("Uploaded file:", uploaded_file)











