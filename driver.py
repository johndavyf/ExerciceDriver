from selenium import webdriver
# if chromedriver is not in your path, you’ll need to add it here
driver = webdriver.Chrome(r'C:\Users\johnd\PycharmProjects\ExerciceDriver\chromedriver.exe')

driver.maximize_window()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title


elePopup = driver.find_element_by_id("at-cv-lightbox-close")
elePopup.click()

eleUserMessage = driver.find_element_by_id("user-message")
eleUserMessage.clear()
eleUserMessage.send_keys("Test Python")

eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
eleShowMsgBtn.click()

eleYourMsg=driver.find_element_by_id("display")
assert "Test Python" in eleYourMsg.text

driver.close()