"""
Program: database.py
Author: Kai Mwirotsi-Shaw
Last date modified: 12/12/2023

This file creates the configuration of mysql connector and home of the cursor.
clear_tables function resides here.

Inserting your database password below is required
"""

import mysql.connector

config = {
    'user': 'root',
    'password': 'insert your database password',
    'host': 'localhost',
    'database': 'News_Articles'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

def clear_tables():
    cursor.execute("DELETE FROM articles")
    db.commit()