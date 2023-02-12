from flask import Flask, render_template, request, url_for
#import class search form
import database, image_append,form, scroll_view
from bs4 import BeautifulSoup
import pandas as pd
import os
import re


global name
#beautiful soup

with open("./templates/Recipes.html") as my_file:
    soup = BeautifulSoup(my_file, "html.parser")




app = Flask(__name__)
@app.route('/Recipes/', methods=[ 'GET', 'POST'])
def Recipes():
   #database.insert_data()


   if request.method == 'POST':
       #clear the form
       form.delete()
       n = request.form['request_data']

       all_data = database.search(str(n))

       form.display(all_data)
       return render_template("search.html", visibility = 'hidden')

   return render_template("Recipes.html")











#pass stuff to file

@app.route('/')
def home():
    return render_template("main.html")

    #redirect to another page using /about/




@app.route('/about/')
def about():
    return render_template("about.html", visibility = "hidden")

@app.route('/Subscribe')
def subscribe():
    return render_template("subscribe.html")







if __name__ == "__main__":
       app.run(debug = True)
