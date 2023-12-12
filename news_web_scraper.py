"""
Program: news_web_scraper.py
Author: Kai Mwirotsi-Shaw
Last date modified: 12/12/2023

This file contains the News_Web_Scraper class which can use BeautifulSoup
to web scrape from the NPR website.
"""

from bs4 import BeautifulSoup
import requests
import database as db
from datetime import datetime
import gui

class News_Web_Scraper:
    def __init__(self,url="https://www.npr.org/sections/science/"):
        self.url = url
        self.result = requests.get(self.url).text

    def set_url_listbox(self,topic):
        match topic:
            case "Business":
                self.url = "https://www.npr.org/sections/business/"
            case "Health":
                self.url = "https://www.npr.org/sections/health/"
            case "Science":
                self.url = "https://www.npr.org/sections/science/"
            case "Books":
                self.url = "https://www.npr.org/books/"
            case "Movies":
                self.url = "https://www.npr.org/sections/movies/"
            case "Television":
                self.url = "https://www.npr.org/sections/television/"
            case "Pop Culture":
                self.url = "https://www.npr.org/sections/pop-culture/"
            case "Food":
                self.url = "https://www.npr.org/sections/food/"
            case "Art & Design":
                self.url = "https://www.npr.org/sections/art-design/"
            case "Performing Arts":
                self.url = "https://www.npr.org/sections/performing-arts/"
            case "Gaming":
                self.url = "https://www.npr.org/sections/gaming/"
            
        self.result = requests.get(self.url).text
    def set_url(self, url):
        self.url = url
        self.result = requests.get(self.url).text
    def find_articles(self):
        titles_length = int()
        titles_text = list()
        href_text = list()
        news = str()
        articles_insert_command = "INSERT INTO articles(href_title, href, creation_date) VALUES (%s, %s, %s)"
        doc = BeautifulSoup(self.result, "html.parser")
        title_tag = doc.find_all('h2', class_ = 'title')
        titles_length = len(title_tag)

        try:
            #Scans html for titles
            for x in range(titles_length):
                titles_text.append(title_tag[x].text)
            if str(titles_text[x]) == "":
                raise Exception

            #Scans html for links
            for tags in doc.find_all('a'):
                if tags.parent.name == 'h2':
                    href_text.append(tags["href"])
        except:
            raise Exception("The URL selected isn't functioning")

        #Inserts into database
        for x in range(titles_length):
            article_info = (str(titles_text[x]), str(href_text[x]), datetime.now())
            db.cursor.execute(articles_insert_command, article_info)
            db.db.commit()
            
    def __str__(self):
        return "Current url:" + self.url

    def __repr__(self):
        titles_length = int()
        titles_text = list()
        href_text = list()
        news = str()

        doc = BeautifulSoup(self.result, "html.parser")
        title_tag = doc.find_all('h2', class_ = 'title')
        titles_length = len(title_tag)

        for x in range(titles_length):
            titles_text.append(title_tag[x].text)
        for tags in doc.find_all('a'):
            if tags.parent.name == 'h2':
                href_text.append(tags["href"])

        for x in range(titles_length):
            news += titles_text[x] + ":\n" + href_text[x] + "\n\n"

        return str(news)