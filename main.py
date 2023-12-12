"""
Program: main.py
Author: Kai Mwirotsi-Shaw
Last date modified: 12/12/2023

This file initiates a News_Web_Scraper class and passes the class to the gui method

Make sure to install BeautifulSoup 4, mysql.connector, and add your database password in database.py
"""

import news_web_scraper as nws
from gui import gui

def main():
    News = nws.News_Web_Scraper()
    gui(News)

if __name__ == "__main__":
    main()