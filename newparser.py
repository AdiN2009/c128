from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

dwarf_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source, "html.parser")
        tr_tags = td_tag.find_all("td")
        temp_list = []
        for index, td_tag in enumerate(td_tags):
            if index == 0:
                temp_list.append(td_tag.find_all('a')[0].content[0])
            else:
                try:
                    temp_list.append(td_tag.contents[0])
                except:
                    temp_list.append("")
            
            dwarf_data_data.append(temp_list)
        
        print(dwarf_data_data[1])






        



        
# Calling Method    
scrape()

# Define Header
headers = ["star_name", "radius", "mass", "distance_data", ]

# Define pandas DataFrame   
dwarf_1 = pd.DataFrame(dwarf_data,columns=headers)
dwarf_1.to_csv('scraped_data.csv',index=True,index_label="id")

# Convert to CSV

    
