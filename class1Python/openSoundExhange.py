import os
from selenium import webdriver

def main():
    value = "1123123"
    firefoxDriver = "..\\FirefoxDriver\\geckodriver.exe"
    browser = webdriver.Firefox(executable_path=firefoxDriver)
    browser.get("https://isrc.soundexchange.com/#!/search")
    browser.maximize_window()


    lookupByCode = browser.find_element_by_id('code-tab')
    lookupByCode.click()

    isrcInput = browser.find_element_by_id('isrcCode')
    isrcInput.send_keys(value)

    lookupButton = browser.find_element_by_id('submit-isrc')
    lookupButton.click()


    # element.clear()
    # element.send_keys('Selenium Webdriver')
    # search_icon = browser.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
    # search_icon.click()

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()