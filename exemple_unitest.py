import unittest
from selenium import webdriver


class InputFormsCheck(unittest.TestCase):

    # Opening browser.
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\johnd\PycharmProjects\ExerciceDriver\chromedriver.exe')
        pageUrl = "https://www.esig-sandbox.ch/team20_3_v2/environnement_dev/index.php"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        # Clicker pour ouvrir le loginForm
        btnToggleNavbar = driver.find_element_by_css_selector(".navbar-toggler-icon")
        btnToggleNavbar.click()
        btnSeConnecter = driver.find_element_by_link_text("Se connecter")
        btnSeConnecter.click()
        # Entrer l'adresse email et le password et valider
        inputEmail = driver.find_element_by_name("email")
        inputEmail.clear()
        inputEmail.send_keys("dreadzbarber3@gmail.com")
        inputPassword = driver.find_element_by_name("password")
        inputPassword.clear()
        inputPassword.send_keys("mdpadmin")
        btnLogin = driver.find_element_by_name("btnLogin")
        btnLogin.click()


    # Testing Single Input Field.
    def test_singleInputField(self):
        pageUrl = "https://www.esig-sandbox.ch/team20_3_v2/environnement_dev/index.php"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)

        btnSeConnecter = driver.find_element_by_link_text("Nouveau client")
        btnSeConnecter.click()


    """ 
        
        # Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        eleUserMessage = driver.find_element_by_id("user-message")
        eleUserMessage.clear()
        eleUserMessage.send_keys("Test Python")

        # Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        eleShowMsgBtn = driver.find_element_by_css_selector('#get-input > .btn')
        eleShowMsgBtn.click()

        # Checking whether the input text and output text are same using assertion.
        eleYourMsg = driver.find_element_by_id("display")
        assert "Test Python" in eleYourMsg.text

    # Closing the browser.
    def tearDown(self):
        self.driver.close()
"""

# This line sets the variable “__name__” to have a value “__main__”.
# If this file is being imported from another module then “__name__” will be set to the other module's name.
if __name__ == "__main__":
    unittest.main()