import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib.request
import os
import time
from instabot import Bot
from datetime import datetime

current_link = 0

while True :

    home_url = "https://metalhangar18.com/site/category/news"
    r1 = requests.get(home_url)
    r1.status_code
    page = r1.content

    soup_link = BeautifulSoup(page, 'html.parser')
    links = soup_link.find_all('div',attrs={'id' : re.compile("^post-20")},limit=1)
    for div in links:
        latest_link = div.a['href']
        print("link:",latest_link)


    post_url = latest_link
    r1 = requests.get(post_url)
    r1.status_code
    post_page = r1.content

    soup_img = BeautifulSoup(post_page, 'html.parser')
    imgs = soup_img.find_all('img',attrs={'class' :  [re.compile("^alignright wp-image-"),re.compile("^aligncenter size-medium wp-image-"),re.compile("^alignleft size-thumbnail wp-image"),re.compile("^alignright size-thumbnail wp-image-")]},limit=1)
    for div in imgs:
        latest_image = div['src']
        print("img:",latest_image)

    urllib.request.urlretrieve(latest_image, "myimg.jpg")

    soup_title = BeautifulSoup(page, 'html.parser')
    titles = soup_title.find_all('h2',attrs={'class' :  'title'},limit=1)
    for div in titles:
        latest_title = div.a['title']
        temp_title = latest_title.split(':')[1]
        latest_title = temp_title
        print("title:",latest_title)

    soup_text = BeautifulSoup(page, 'html.parser')
    texts = soup_text.find('div',attrs={'class' :  'post-content clear-block'}).getText()
    print("text:",texts)

    time.sleep(5)
  
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)


    while current_link != latest_link:
        bot = Bot()
        print("shu se ka4va v ig")
        bot.login(username = """"your instagram username"""",password = """"your instagram password"""")
        caption = latest_title + "\n\n" + texts + latest_link
        bot.upload_photo("myimg.jpg",caption)
        #print(latest_title + texts + latest_link )
        current_link = latest_link
        if os.path.exists("myimg.jpg.REMOVE_ME"):
            os.remove("myimg.jpg.REMOVE_ME")
        else:
            print("The file does not exist")

    time.sleep(1200)
