"""
Program: unit_test.py
Author: Kai Mwirotsi-Shaw
Last date modified: 12/12/2023

This file tests the News_Web_Scraper class
"""

import unittest
import news_web_scraper as nsw

class News_Web_Scraper_Test_Case(unittest.TestCase):
    def setUp(self):
        self.News = nsw.News_Web_Scraper("https://www.npr.org/sections/science/")
    def tearDown(self):
        del self.News
    def test_broken_links(self):
        with self.assertRaises(Exception):
            self.setUp()
            self.News.set_url("https://www.npr.org/sections/error/")
            self.News.find_articles()
    def test_student_repr(self):
        self.setUp()
        print(repr(self.News))
    def test_student_str(self):
        self.setUp()
        print(str(self.News))

if __name__ == '__main__':
    unittest.main()