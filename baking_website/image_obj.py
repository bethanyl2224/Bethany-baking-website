from bs4 import BeautifulSoup
import pandas as pd



all_object = []

data = pd.read_csv("info.csv")
address = list(data['link'])
image_ip = list(data['img_ip'])
title = list(data['title'])



class img_obj:

    def __init__(self, address, image_ip, title):
       self.address = address
       self.image_ip = image_ip
       self.title = title


for i in range(len(title)):
    all_object.append(img_obj(address[i], image_ip[i], title[i]))



class img_soup:
    def __init__(self, pathway):
       self.pathway = pathway

    def reset(self, attrs):
        for div in self.find_all("div", attrs = {"class": str}):
            div.decompose()


    def template(self):
        insert_code = """ <div class={na}>
        <a href="{link}">
        <img alt="can't find img" class="{na}" img="" src={src}/>
        </a>
        <label class="label_recipe">
        {quote}
        </label>
        </div> """
        return insert_code

    def find(self, class_name):
        self.insert = self.find_all("div", attrs = {"class": str(class_name)})




    def update(self):
      with open("./templates/{}".format(self.pathway), "wb") as my_file:
          my_file.write(self.prettify("utf-8"))

    def display(self):
        return self
