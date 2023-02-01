from bs4 import BeautifulSoup
from image_append import reset
import pandas as pd
import image_obj as img
from image_append import reset


with open("./templates/main.html") as my_file:
      soup2 = BeautifulSoup(my_file, "html.parser")

reset("recipe", soup2)


info = ['Delicious glutinous rice with sweet mango and coconut taste", ''Perfect flourless blueberry Pancakes', 'The irrestible taste of the coconut infusing in the bread', 'Home-made garlic butter with crispy bread', 'Traditional coconut glutinous rice ball with sweet red bean', "Family-size sweet bread made with 100% real honey", "Explore 3 ways to make chia seed pudding", "Japanese-inspired matcha bread that melts in your mouth"]


def init():

   recipe_scroll = soup2.find("div", attrs = {"class": "newest_recipe_scroll"})




   html = """ <div class={na}>
  <a href="{link}">
 <img alt="can't find img" class="{na}" img="" src={src}/>
 </a>
 <label class = "label_scroll">
 {quote}
 </label>

 <label class = "recipe_description">
 {description}


 </label>

</div> """

   for i in range(6):

          recipe_scroll.append(BeautifulSoup(html.format(link = img.all_object[i].address,  quote = img.all_object[i].title, na = "recipe", description= info[i], src = img.all_object[i].image_ip), "html.parser")
)



   with open("./templates/main.html", "wb") as my_file:
       my_file.write(soup2.prettify("utf-8"))
init()
