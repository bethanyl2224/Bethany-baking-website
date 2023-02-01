from instagramy import InstagramUser
import json
import cv2
import numpy as np
import urllib
from convert_cv import convert_image
user = InstagramUser("bethcookingvlog", from_cache=True)


with open(".instagramy_cache/bethcookingvlog_user.json") as myfile:
    my_file = json.load(myfile)

#find all keys

#print(my_file.keys())

# get video_url(to the post), display_url(pictures)
print(user.posts[0].display_url)
image = convert_image(user.posts[0].display_url)
cv2.imshow('hello', image)


#video_url = my_file['video_url']
#titles = my_file['edge_media_to_caption']
#print(titles)
