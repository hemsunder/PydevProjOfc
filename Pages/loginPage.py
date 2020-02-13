class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.username_textbox_name = "loginRequestBean.userId"
        self.driver.password_textbox_name = "loginRequestBean.password"
        self.driver.storeid_textbox_name = "loginRequestBean.locNbr"
        self.driver.login_btn = "login"
        
    def login(self, un, pwd, stid):
        self.driver.find_element_by_name(self.driver.username_textbox_name).send_keys(un)
        self.driver.find_element_by_name(self.driver.password_textbox_name).send_keys(pwd)
        self.driver.find_element_by_name(self.driver.storeid_textbox_name).send_keys(stid)
        self.driver.find_element_by_name(self.driver.login_btn).click()
        assert self.driver.title == "QFund"
        
# login = LoginPage("driver")
# print(login.driver)