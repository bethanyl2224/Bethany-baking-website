from bs4 import BeautifulSoup
import pandas as pd
import sqlite3




global my_link, address, name

with open("./templates/Recipes.html") as my_file:
    soup = BeautifulSoup(my_file, "html.parser")

tag = soup.new_tag('br')
parent = soup.find_all("label")
data = pd.read_csv("info.csv")
image_ip = list(data['img_ip'])
ipaddress = list(data['link'])
title = list(data['title'])


#print(address, name)


def create_data():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS database (id INTEGER PRIMARY KEY, name text, img_ip text, link text)")
    conn.commit()
    conn.close()



def clear_all():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DROP TABLE database")
    conn.commit()
    conn.close()


#clear_all()






def display():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM database")
    rows = cur.fetchall()
    conn.close()
    return rows


#cur.execute("CREATE TABLE IF NOT EXISTS image (id INTEGER PRIMARY KEY, img_name text, ipaddress text, name text , type text)")



def search(na=""):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    #pass the parameter into the database
    #cur.execute("SELECT * FROM image WHERE name = ? or type = ?", (na, ty))

    cur.execute("SELECT * FROM database WHERE name LIKE (?)", ('%{}%'.format(na),))
    rows = cur.fetchall()
    #print(rows)
    conn.close()
    return rows





def insert_data():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM database")
    rows = cur.fetchall()



    ip = []
    #append all available ipaddress in the database
    for i in range(len(rows)):

        ip.append(rows[i][3])
    for i in range(len(ipaddress)):
        # insert new data into data base
        if not ipaddress[i] in ip:
            #cur.execute("INSERT INTO book VALUES (Null, ?,?,?,?)", (title, author,year, isbn))

            cur.execute("INSERT INTO database VALUES (Null, ?,?, ?)",(title[i], image_ip[i], ipaddress[i]))
            #execute the init() function -> alter html documents



    conn.commit()
    conn.close()


'''


def display():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM images")
    rows = cur.fetchall()
    conn.close()
    return rows


create_data()
insert_data()
display()
'''
#search('mochi')

#create_data()
#clear_all()
#create_data()

insert_data()
#print(display())


#insert_data()

#search('Purple Yam Swirl Bread')

    # (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)
