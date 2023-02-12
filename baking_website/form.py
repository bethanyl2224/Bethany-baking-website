import database
from bs4 import BeautifulSoup
import image_append



with open("./templates/search.html") as my_file:
    soup = BeautifulSoup(my_file, "html.parser")

def delete():
    """
    Delete all recipes in the recipe.html
    """
    for div in soup.find_all("div", attrs = {"class": "recipe"}):
        div.decompose()
   


def display(data):
    """
    Fetch all of the display data and modify the search.html file
    """
    insert_place = soup.find('div', {'class' : 'info'})
    #print(insert_place)

    for id, name, img_ip, link in data:

        html = """ <div class= "recipe">
        <a href="{link}">
        <img alt="can't find img" class="na" img="" src={src}/>
        </a>
        <label class="label_recipe"> {info}
        </label>
        </div> """.format( na = name, info = name, link = link, src = img_ip)
        insert_place.append(BeautifulSoup(html, "html.parser"))

    with open("./templates/search.html", "wb") as my_file:
            my_file.write(soup.prettify("utf-8"))


