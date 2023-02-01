all_soup = []
pathway = ["Recipes.html", "main.html"]

for path in pathway:
    with open("./templates/{path}".format(path= path)) as my_file:
      all_soup.append(BeautifulSoup(my_file, "html.parser"))




#reset

def reset(attrs, soup):
    for div in soup.find_all("div", attrs = {"class": str}):
        div.decompose()

try:
  reset("recipe", all_soup[0])
  reset("line-break", all_soup[1])
  reset("recipe", all_soup[1])
except:
    pass


def init():

    html = """ <div class={na}>
    <a href="{link}">
    <img alt="can't find img" class="{na}" img="" src={src}/>
    </a>
    <label class="label_recipe">
    {quote}
    </label>
    </div> """

    class_insert = all_soup[0].find("div", {"class": "info"})
    scroll_insert = all_soup[1].find("div", {"class": "newest_recipe_scroll"})
    print(class_insert, scroll_insert)


    for i in range(0, len(img.all_object)):

        class_insert.append(BeautifulSoup(html.format(link = img.all_object[i].address,  quote = img.all_object[i].title, na = "recipe", src = img.all_object[i].image_ip), "html.parser"))
    for i in range(0,2):
        scroll_insert.append(BeautifulSoup(html.format(link = img.all_object[i].address,  quote = img.all_object[i].title, na = "recipe", src = img.all_object[i].image_ip), "html.parser"))



    #modify html file

init()
print(all_soup)

for soup in all_soup:
    print("_______________________", soup)

def update():
    for path in pathway:
        for soup in all_soup:
          with open("./templates/{path}".format(path= path), "wb") as my_file:
              my_file.write(soup.prettify("utf-8"))


#update()
