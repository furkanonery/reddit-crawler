from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from celery import shared_task
from bs4 import BeautifulSoup
from crawler_soup.celery import logger
from celery.utils.log import logging
from crawler_soup.models import Subreddits
from selenium.webdriver.common.by import By


@shared_task
def getposts():

    logger.info("Başladı...")

    subreddit = "Home"
    
    url = f"https://www.reddit.com/r/{subreddit}/new/"

    chrome_options = Options()
    chrome_options.add_argument("--headless")


    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    time.sleep(30)

   
    scroll_pause_time = 1
    scroll_count = 0
    max_scroll_count = 5


    while scroll_count < max_scroll_count:
        time.sleep(scroll_pause_time)
        scroll_count += 1



    content = driver.page_source

    driver.quit()

    time.sleep(30)

    soup = BeautifulSoup(content, 'html.parser')

    time.sleep(30)


    posts = soup.find_all('div', {'data-testid': 'post-container'})

    time.sleep(10)

    len_posts=len(posts)

    if(len_posts>0):
        for post in posts:
            title = post.find('h3', {'class': '_eYtD2XCVieq6emjKBH3m'})

            subreddit_post = Subreddits(
                    title=title.getText(),
                    subreddit="Test"
                )
            subreddit_post.save()
            
            logger.info("Başlık: %s", title.getText())
        