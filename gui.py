"""
Program: gui.py
Author: Kai Mwirotsi-Shaw
Last date modified: 12/12/2023

This file creates the gui. Features a listbox which populates with news articles and links.
The listbox can be cleared or populated with selected news topics.

logo source: https://www.pngall.com/sunshine-png/
"""

import database as db
from tkinter import *
import webbrowser


def gui(News):
    root = Tk()
    root.title('Your Daily News')
    root.iconbitmap("sunshine.ico")

    news_listbox1 = Listbox(root)
    news_listbox1.pack(pady=15)
    news_listbox1.grid(sticky=(N, S, E, W), row=1)
    root.columnconfigure(0, weight=1)

    clicked = StringVar()
    clicked.set("Science")
    drop_down_menu = OptionMenu(root, clicked, "Business", "Health", "Science", "Books", "Movies", "Television", "Pop Culture", "Food", "Art & Design", "Performing Arts", "Gaming")
    drop_down_menu.grid(row=2)
    button1 = Button(root, text='Find News Articles', width=15, command= lambda: article_listbox_find_and_insert())
    button1.grid(row=3)
    button2 = Button(root, text='Clear Table', width=15, command= lambda: clear_listbox())
    button2.grid(row=4)

    def clear_listbox():
        news_listbox1.delete(0,END)
        db.clear_tables()

    def weblink(*args):
        index = news_listbox1.curselection()[0]
        item = news_listbox1.get(index)
        if 'https://' in item:
            webbrowser.open_new(item)

    def article_listbox_insertion():
        news_listbox1.delete(0,END)
        db.cursor.execute("select href_title from articles")
        href_title_result = db.cursor.fetchall()
        db.cursor.execute("select href from articles")
        href_result = db.cursor.fetchall()
        db.cursor.execute("select DATE(creation_date) from articles")
        date_result = db.cursor.fetchall()
        news_listbox1.bind('<<ListboxSelect>>', weblink)
        #The data is first filtered for unecessary characters, then inserted into database
        for x in range(len(href_title_result)):
            chars_to_remove = "()',"
            chars_to_remove_datetime = "()',mdatei."
            for char in chars_to_remove:
                href_title_result[x] = str(href_title_result[x]).replace(char, "")
                href_result[x] = str(href_result[x]).replace(char, "")
            for char in chars_to_remove_datetime:
                date_result[x] = str(date_result[x]).replace(char, "")
            date_result[x] = str(date_result[x]).replace(' ', '/')
            news_listbox1.insert(END, str(href_title_result[x]+' (Added: '+ date_result[x] + ')'))
            news_listbox1.insert(END, str(href_result[x]))
            news_listbox1.itemconfig(END, bg = "deep sky blue", fg='black')
    
    def article_listbox_find_and_insert():
        News.set_url_listbox(clicked.get())
        News.find_articles()
        article_listbox_insertion()

    article_listbox_insertion()      

    root.mainloop()