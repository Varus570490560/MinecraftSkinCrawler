import time

import bs4
import cloudscraper as cloudscraper
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

drivers = []
scraper = cloudscraper.create_scraper()


def get_soup(url: str, use_chrome: bool = True, features='html.parser'):
    content = get_page_source(url, use_chrome=use_chrome)
    soup = bs4.BeautifulSoup(content, features=features)
    return soup


def get_page_source(url: str, use_chrome: bool = True):
    print('open url %s' % url)
    if use_chrome:
        if not drivers:
            drivers.append(webdriver.Chrome(options=chrome_options, desired_capabilities=caps))
        driver = drivers[0]
        driver.get(url)
        print(driver.window_handles)
        while True:
            source = driver.page_source

            if 'DDoS protection' in source:
                print('wait for DDoS protection')
                time.sleep(0.5)
            else:
                break
        return source
    else:
        return scraper.get(url).content
