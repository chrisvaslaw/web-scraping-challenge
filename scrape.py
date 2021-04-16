from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init():
    # initiate splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

# Create dictionary to hold data
mars_data = {}

def mars_news():
    
    # initiate browser
    browser = init()
    
    # Visit redplanetscience.com/
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the Latest News Title
    title = soup.find("div", class_="content_title").get_text()

    # Get the Latest Paragraph Text
    paragraph = soup.find("div", class_="article_teaser_body").get_text()
    
    # Add to Mars Data Dictionary
    mars_data['title'] = title 
    mars_data['paragraph'] = paragraph
    
    # Close Browser and Return Data
    browser.quit()
    return mars_data
#__________________________________________________________________________________#

def mars_image():
    
    # initiate browser
    browser = init()
    
    # Visit https://spaceimages-mars.com/
    url = "https://spaceimages-mars.com/"
    featured_image_url = url + ('image/featured/mars3.jpg')
    browser.visit(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # Get the current Featured Mars Image
    featured_image = soup.find_all('img')[1]["src"]
    
    # Add to Mars Data Dictionary
    mars_data['image'] = featured_image_url + featured_image
    
    # Close Browser and Return Data
    browser.quit()
    return mars_data
    
#__________________________________________________________________________________#

def mars_facts():
    
    # initiate browser
    browser = init()
    
    # Visit https://galaxyfacts-mars.com/
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    time.sleep(1)
    
    # Use pandas read html for Mars Planet Profile
    mars_facts_profile = pd.read_html(url)[1]

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the remaining facts about the planet
    mars_facts_list = soup.find_all("ul", class_="mt-3")
    
    # Add to Mars Data Dictionary
    mars_data['quick_facts'] = mars_facts_profile
    mars_data['fun_facts'] =  mars_facts_list
    
    # Close Browser and Return Data
    browser.quit()
    return mars_data