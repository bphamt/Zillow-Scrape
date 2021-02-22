from selenium import webdriver
import time

CHROME_DRIVER_PATH = r"C:\Users\bpham\Documents\chromedriver"
URL_SCRAPE = "https://forms.gle/JaJc8Xh23Yw9aQKL9"

class Insert:
    def __init__(self, price_list, address_list, url_list):
        self.price_list = price_list
        self.address_list = address_list
        self.url_list = url_list

    def fill_form(self, index):
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        driver.get(URL_SCRAPE)

        # Sleep for 3 seconds to allow Google Sheets to load
        time.sleep(3)

        # Enter data into form field
        address_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_field.send_keys(self.address_list[index])

        price_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_field.send_keys(self.price_list[index])

        link_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_field.send_keys(self.url_list[index])

        # Click submit button
        button_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        button_field.click()

        # Close screen after completion
        driver.close()