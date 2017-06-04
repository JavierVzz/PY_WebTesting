import os
from selenium import webdriver

def main():
    firefoxDriver = "..\\FirefoxDriver\\geckodriver.exe"
    browser = webdriver.Firefox(executable_path=firefoxDriver)
    browser.get("https://www.amazon.com/")
    browser.maximize_window()

    text = browser.find_element_by_class_name("nav_a").text
    print(text)

    # element = browser.find_element_by_id('twotabsearchtextbox')
    # element.clear()
    # element.send_keys('Selenium Webdriver')
    # search_icon = browser.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
    # search_icon.click()

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()