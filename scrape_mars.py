from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
     Set Executable Path & Initialize Chrome Browser
    executable_path = {"executable_path": "./chromedriver.exe"}
    return Browser("chrome", **executable_path)


# # Set Executable Path & Initialize Chrome Browser
# executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
# browser = Browser("chrome", **executable_path, headless=False)


def Mars_News():
    browser = init_browser()

    # Visit Mars.nasa.Gov
      nasa_url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    mars_news_info = {}
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html.parser")

    #scrapping infos about mars from nasa.Gov
    news_title = soup.find("div",class_="content_title").text
    news_paragraph = soup.find("div", class_="article_teaser_body").text
    mars_news_info['news_title'] = news_title
    mars_news_info['news_paragraph'] = news_paragraph 

     #Mars  Image scrapping
    nasa_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(nasa_image)
    time.sleep(1)
     # Click through to full image
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Search for image source
    results = soup.find_all('figure', class_='lede')
    relative_img_path = results[0].a['href']
    Mars_img = 'https://www.jpl.nasa.gov' + relative_img_path

# Mars Facts Web Scraper
def mars_facts():
    # Visit the Mars Facts Site Using Pandas to Read
    try:
        df = pd.read_html("https://space-facts.com/mars/")[0]
    except BaseException:
        return None
    df.columns=["Description", "Value"]
    df.set_index("Description", inplace=True)

# Helper Function
# Service Temporarily Unavailable
# page down

    return df.to_html(classes="table table-striped")

