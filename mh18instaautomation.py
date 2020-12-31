import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import urllib.request
import os
import time
from instabot import Bot
from datetime import datetime
import http.client
import sys
import config

current_link = 0
latest_image = 0
#it needs a base url because its undeclared
latest_link = "http://google.com"
bot = Bot()
bot.login(username = config.username, password = config.password)

def send(image_url):
    webhook = DiscordWebhook(url=config.webhookurl)
    # create embed object for webhook
    embed = DiscordEmbed(title="MH18 insta", description="<@&693878676785463297>" + " a new post has been uploaded to instagram via your script", color=242424)

    # add embed object to webhook
    webhook.add_embed(embed)
    embed.set_image(url=image_url)
    response = webhook.execute()

while True :

    home_url = "https://metalhangar18.com/site/category/news"
    r1 = requests.get(home_url)
    r1.status_code
    page = r1.content

    soup_link = BeautifulSoup(page, 'html.parser')

    links = soup_link.find_all('div',attrs={'id' : re.compile("^post-21")},limit=1)
    for div in links:
        latest_link = div.a['href']
        print("link:",latest_link)

    post_url = latest_link
    r1 = requests.get(post_url)
    r1.status_code
    post_page = r1.content

    soup_img = BeautifulSoup(post_page, 'html.parser')
    imgs = soup_img.find_all('img',attrs={'class' :  [re.compile("^alignright wp-image-"),re.compile("^aligncenter size-medium wp-image-"),re.compile("^alignleft size-thumbnail wp-image"),re.compile("^alignright size-thumbnail wp-image-"),re.compile("^size-medium wp-image-20")]},limit=1)
    if not imgs:
        for div in imgs:
            latest_image = div['src']
            print("img:",latest_image)
            urllib.request.urlretrieve(latest_image, "myimg.jpg")
    else:
            soup_img = BeautifulSoup(page, 'html.parser')
            imgs = soup_img.find_all('img',attrs={'class' :  [re.compile("attachment-post-thumbnail size-post-thumbnail wp-post-image")]},limit=1)
            for div in imgs:
                latest_image = div['src']
                latest_image = latest_image.replace("120x120","500x500")
                print("img:",latest_image)
                myfile = requests.get(latest_image)
                open('myimg.jpg', 'wb').write(myfile.content)

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
    time.sleep(1200)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    if(latest_image == 0):
        time.sleep(5)
        print("going to sleep")

    while current_link != latest_link and latest_image!=0:

        print("shu se ka4va v ig")
        caption = latest_title + "\n\n" + texts + "За повече информация и пълния пост посетете сайта ни metalhangar18.com или цъкнете линка в профила ни!"
        try:
            bot.upload_photo("myimg.jpg",caption)
            send(latest_image)
        except:
            pass

        current_link = latest_link;

        time.sleep(12)
        break
