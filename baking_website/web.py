from flask import Flask, render_template, request, url_for
#import class search form
import database, image_append,form, scroll_view
from bs4 import BeautifulSoup
import pandas as pd
import os



global name


app = Flask(__name__)
@app.route('/Recipes/', methods=[ 'GET', 'POST'])
def Recipes():
   #database.insert_data() - test in database insert correctly

   if request.method == 'POST':
       #clear the form if button click
       
       form.delete()
       #fetch request keyword from the user
       n = request.form['request_data']
        
       #search this particular data in the database, then display it

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
