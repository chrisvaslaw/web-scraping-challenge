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
    
    # Close Browser and Return Data
    browser.quit()
    return title, paragraph
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
    featured_image_path = soup.find_all('img')[1]["src"]
    featured_image = url + featured_image_path
    
    # Close Browser and Return Data
    browser.quit()
    return featured_image, featured_image_url
    
#__________________________________________________________________________________#

def mars_facts():
    
    # initiate browser
    browser = init()
    
    # Visit https://galaxyfacts-mars.com/
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    time.sleep(1)
    
    # Use pandas read html for Mars Planet Profile
    mars_facts_profile = pd.read_html(url)[0].to_html()

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the remaining facts about the planet
    mars_facts_list = soup.find_all("ul", class_="mt-3")
    for facts in mars_facts_list:
    # Loop through facts list to get text and add to Mars Data
        facts_text = facts.text

    # Add Profile Facts to Mars Data Dictionary
    
    # Close Browser and Return Data
    browser.quit()
    return mars_facts_profile, facts_text

#__________________________________________________________________________________#

def scrape_all():
       
    browser = init()
    
    title, paragraph = mars_news()
    featured_image, featured_image_url = mars_image()
    mars_facts_profile, facts_text = mars_facts()

    data = {
        "news_title": title,
        "news_paragraph": paragraph,
        "featured_image": featured_image,
        "facts_profile": mars_facts_profile,
        "facts_list": facts_text
                        }
    browser.quit()
    return data 

if __name__ == "__main__":
    print(scrape_all())