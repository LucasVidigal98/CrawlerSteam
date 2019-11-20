from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()
options.set_headless(headless=True)
options.binary = binary
firefox = webdriver.Firefox(capabilities=cap, executable_path= '/usr/local/bin/geckodriver')
firefox.get('https://steamcommunity.com/app/730/reviews/')

teste = firefox.firefox.find_elements_by_class_name('apphub_GetMoreContent')
print(teste)