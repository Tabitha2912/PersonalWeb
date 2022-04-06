from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import urllib.request
import json

s = Service("D:/Kuliah/Semester 2/Proyek 1/Pertemuan 6/Tugas 6.3/msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get("https://editorial.rottentomatoes.com/guide/best-disney-movies-to-watch-now/")

# now = datetime.now()
# tgl = now.strftime("%m/%d/%Y, %H:%M:%S")
# movie=[]
# i=1

content=driver.find_elements(By.CLASS_NAME, "row.countdown-item")
for movielist in content:
        print(movielist.text.split("\n"))
        for img in movielist.find_elements(By.TAG_NAME,"img"):
                print(img.get_attribute("src"))
                # urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
                #i = i+1
#          movie.append(
#                      {"Ranking":movielist.text.split("\n")[2].split("#",1)[1],
#                              "Title":movielist.text.split("\n")[0].split(" (",1)[0],
#                              "Release_Date":movielist.text.split("\n")[0].split(" (", 1)[1].split(")")[0],
#                              "Percent_Rate":movielist.text.split("\n")[1],
#                              "Director":movielist.text.split("\n")[6].split("Directed By: ",1)[1],
#                              "Scraping_Date":tgl,
#                              "Image": img.get_attribute("src")
#  					}
#  				)

# hasil_scraping = open("hasilscraping.json", "w")
# json.dump(movie, hasil_scraping, indent = 6)
# hasil_scraping.close()

driver.quit()

