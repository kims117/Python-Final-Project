"""
Program: setup.py
Author: Kai Mwirotsi-Shaw
Last date modified: 12/12/2023

This file creates sets up the News_Articles database and the articles table.
"""

import mysql.connector
from database import cursor
from mysql.connector import errorcode

DB_NAME = 'News_Articles'

TABLES = {}

TABLES['articles'] = ("""
    CREATE TABLE articles (
    article_id INT AUTO_INCREMENT PRIMARY KEY,
    href_title VARCHAR(250) NOT NULL,
    href VARCHAR(250) NOT NULL,
    creation_date DATETIME NOT NULL)
    """
)

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({})".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)
create_database()
create_tables()