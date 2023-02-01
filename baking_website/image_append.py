from bs4 import BeautifulSoup
import pandas as pd
import image_obj as img



with open("./templates/Recipes.html") as my_file:
    soup = BeautifulSoup(my_file, "html.parser")
#print(soup)


def reset(str, soup):
    #soup.find("div", {"class": "info"});
    #print("before", soup.find("div", {"class": "info"}))

    #delete only the attribute of the class
    for div in soup.find_all("div", attrs = {"class": str}):
        div.decompose()

try:
  reset("recipe", soup)
  reset("line-break", soup)
  #reset("newest_recipe_scroll", soup2)
except:
    pass









#print(soup)
def init():

    data = pd.read_csv("info.csv")
    address = list(data['link'])
    image_ip = list(data['img_ip'])
    title = list(data['title'])
    #print(address, name)

    


    #all_images = os.listdir("./static/pictures")
    #print(all_images)

    html = """ <div class={na}>
   <a href="{link}">
  <img alt="can't find img" class="{na}" img="" src={src}/>
  </a>
  <label class="label_recipe">
    {quote}
  </label>
 </div> """


    class_insert = soup.find("div", {"class": "info"});


    for i in range(0, len(title)):

            class_insert.append(BeautifulSoup(html.format(link = img.all_object[i].address,  quote = img.all_object[i].title, na = "recipe", src = img.all_object[i].image_ip), "html.parser"))

    #for i in range(0,2):
         #scroll_view.insert.append(BeautifulSoup(html.format(link = all_object[i].address,  quote = all_object[i].title, na = "recipe", src = all_object[i].image_ip), "html.parser"))

    #print(soup)


    #modify html file


    with open("./templates/Recipes.html", "wb") as my_file:
        my_file.write(soup.prettify("utf-8"))




   #create search class first
init()
