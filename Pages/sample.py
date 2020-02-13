from selenium import webdriver

driver = webdriver.Ie(executable_path="C:/Selenium WebDriver/Drivers/IEDriverServer.exe")
driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(30)
driver.set_page_load_timeout(30)
driver.get("https://qclocalsprint.qfund.net/cc/demoIndex.do")
print(driver.title)
driver.switch_to.frame()



