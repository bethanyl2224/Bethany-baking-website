from selenium import webdriver
from bs4 import BeautifulSoup
#from webdriver_manager.chrome import ChromeDriverManager






urls = [
'Bethany-sBaking'
]




class VideoObject:
  def __init__(self, title, time, link, type):
      self.title = title
      self.time = time
      self.link = link

      self.type = type

  def print_all(self):
      print("title: " + self.title + "\n" +
             "time " + self.time + "\n"
             + "link " + self.link + "\n"
             + "type " + self.type


      )





def main():
    info = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/c/Bethany-sBaking/videos?view=0&sort=dd&flow=grid')
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    print(soup)
    titles = soup.findAll('a', id = 'video-title')
    views= soup.findAll('span', class_ = 'style-scope ytd-grid-video-renderer')
    video_urls = soup.findAll('a', id = 'video-title')






    i = 0 #views
    j = 0 #urls


    for title in titles:
        text = "Views:" + views[i].text + "Date:" +  views[i+1].text
        my_title = title.text
        my_type = "video"
        if "#" in title.text:
            my_title = my_title[: my_title.index("#")]
        if "shorts" in video_urls[j].get("href"):
            my_type = "short"



        video = VideoObject(title = my_title, time =  text , link = "http://youtube.com{url}".format(url = video_urls[j].get("href")), type = my_type)
        #info.append(video)
        i+=2
        j+=1
    #print(titles)

    # title
    #print(titles[0].text)

    #view (views, and the year)
        #print(views[0].text, view[1].text)
    return info

main()
'''
for int in main():
    int.print_all()

'''
