from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
import pafy
import pandas as pd
import os
import cv2
import numpy as np
import urllib
from urllib.request import urlopen


urls = [
'Bethany-sBaking'
]

"""
Pafy -> use to get youtube metadata


"""

session = HTMLSession()
response = session.get('https://www.youtube.com/c/Bethany-sBaking/videos?view=0&sort=dd&flow=grid')
response.html.render(sleep=1)
soup1 = bs(response.html.html, "html.parser")
urls = soup1.findAll('a', id = 'video-title')
image_url = []


#Note: not getting the Youtube short video for some reason
def get_all_urls(arr):
    """
    get all_urls of the videos display on the Youtube Channel
    """
     urls = []
     for i in range(len(arr)):

        if  not "shorts" in  arr[i].get("href"):
           urls.append("http://youtube.com{url}".format(url = arr[i].get("href")))
     return urls



def init_url():
    #url that we can use to fetch image and display on the website
    image_url = []
    for i in range(len(os.listdir('static/All_Images'))):
        image_url.append('http://127.0.0.1:5000/static/All_Images/image{num}.jpg'.format(num = str(i)))



    return image_url



image_url = init_url()


def url_to_image(arr):
      """
      convert url_to_image and save in local directory
      
      """

      i = 0
      #opencv format
      #download image, convert to a numpy array, and then read and export to local directory
      for url in arr:
        video = pafy.new("{}".format(url))

        name = str("image" + str(i) + ".jpg")
        if not name in image_url:
            resp = urllib.request.urlopen(video.bigthumbhd)
            image = np.asarray(bytearray(resp.read()), dtype = "uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            path = '/Users/bethany/Desktop/baking_website_testing/static/All_Images/{na}'.format(na = name)
            cv2.imwrite(path, image)
        i+=1

image_url = init_url()








def get_info(arr):
    #export all extract info 
    info = {'title': [], 'img_ip': [], "link": []}

    for i in range(len(arr)):
             video = pafy.new("{}".format(arr[i]))
             #info['{}'.format(video.title)] = (VideoObject(video.title, video.bigthumbhd, url))


             info['title'].append(video.title)
             info['img_ip'].append(image_url[i])
             info['link'].append(arr[i])





    return info




video_urls = get_all_urls(urls)
#print(video_urls)

#call the add image function
#url_to_image(video_urls)
all_info = get_info(video_urls)



data = pd.DataFrame(all_info)

#convert data into info.csv file
data.to_csv("/Users/bethany/Desktop/baking_website_testing/info.csv")




#image url created
#print(video_urls)

#thumbnail created


#print(len(thumbnail))
