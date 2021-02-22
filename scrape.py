from selenium import webdriver
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
CHROME_DRIVER_PATH = r"C:\Users\bpham\Documents\chromedriver"
URL_SCRAPE = "https://www.zillow.com/woodbridge-va/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Woodbridge%22%2C%22mapBounds%22%3A%7B%22west%22%3A-77.51161481103516%2C%22east%22%3A-77.10992718896485%2C%22south%22%3A38.53861390400762%2C%22north%22%3A38.762229965463874%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A14701%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A910286%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class Scrape:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(URL_SCRAPE)

    def grab_price(self):
        # Grab zillow prices
        price_list = []
        response = self.driver.find_elements_by_class_name("list-card-price")
        for i in response:
            splitting = ((((i.text.split("$"))[1]).split("/")[0]).split("+")[0]).split()[0]
            price = locale.atoi(splitting)
            price_list.append(price)
        return price_list

    def grab_address(self):
        # Grab zillow addresses
        address_list = []
        response = self.driver.find_elements_by_class_name("list-card-addr")
        for i in response:
            address_list.append(i.text)
        return address_list

    def grab_url(self):
        # Grab zillow url
        url_list = []
        response = self.driver.find_elements_by_css_selector(".list-card-info a")
        for i in response:
            url_list.append(i.get_attribute("href"))
        return url_list
