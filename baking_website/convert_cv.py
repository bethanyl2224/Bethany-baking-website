import cv2
import numpy as np
import urllib

from urllib.request import urlopen



def url_to_image(url,name):

      #opencv format
      #download iamge, convert to a numpy array, and then read
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype = "uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        path = '/Users/bethany/Desktop/baking website testing/All_Images/{na}'

        all_image.append(path)
        cv2.imwrite(path, image)
        return all_images






url_to_image('http://i.ytimg.com/vi/lhaOkG94NI8/hqdefault.jpg')
