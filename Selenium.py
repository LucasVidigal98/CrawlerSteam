from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

'''
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()
options.set_headless(headless=True)
options.binary = binary
'''
firefox = webdriver.Firefox()
firefox.get('https://steamcommunity.com/app/730/reviews/?filterLanguage=brazilian')

teste = firefox.find_elements_by_class_name('apphub_GetMoreContent')
print(teste)