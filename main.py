from data import Data
from insert import Insert
from scrape import Scrape

# Scrape object creation to scrape sites
scrape = Scrape()

# Class that holds the data
data = Data(scrape.grab_price(), scrape.grab_address(), scrape.grab_url())

# Close scrape driver after finish scrapping
scrape.driver.close()

# Insert data into insert class
insert = Insert(data.price_list, data.address_list, data.url_list)

# For loop to insert all data into Google Forms
for i in range(len(data.price_list)):
    insert.fill_form(i)
