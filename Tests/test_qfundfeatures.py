import pytest
from Utilities import utilities as utils
from Pages.loginPage import LoginPage
from Pages.registrationPage import Registration

@pytest.mark.usefixtures("test_setup")
class TestQfundApplication:
    
#     @pytest.mark.skip    
    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(utils.username, utils.password, utils.storeid)
#     @pytest.mark.skip
    def test_registration(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(utils.username, utils.password, utils.storeid)
        reg = Registration(driver)
        reg.registration()
  
