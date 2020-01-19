#python bot for insta/twitter likes
#to run: Desktop\pythonbot\instabot.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup, SoupStrainer
import urllib3
import re
from urllib.request import urlopen

class Instabot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?next=/explore/')
        time.sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
    def like(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+ hashtag +'/') #keyword search
        time.sleep(2)
        for i in range(0, 3):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i = 1
            time.sleep(2)
            #for some reason this lasts like only 2 scrolls idk why.. but fuck it
        posts = bot.find_elements_by_xpath("//a[@href]")
        links = [elem.get_attribute("href") for elem in posts]
        links = [posts for posts in links if posts.startswith('https://www.instagram.com/p/')]
        print (links)
        for link in links:
            bot.get(link)
            try:    
                bot.find_element_by_xpath('//button[@class="wpO6b "]/*[name()="svg"][@aria-label="Like"]').click() 
                time.sleep(10) 
            except Exception as ex:
                time.sleep(60)
ed = Instabot('[Insert Username Here without Brackets]','[Insert Password Here without brackets]')
ed.login()
ed.like('[Insert Hashtag/whatnot here without brackets]')
#bot can be used in other ways such as for following people etc