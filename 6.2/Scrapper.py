#Import package requests dan BeautifulSoup
import requests 
from bs4 import BeautifulSoup

# Request ke website
page = requests.get("https://www.republika.co.id/");

# Extract konten menjadi objek BeautifulSoup
obj = BeautifulSoup(page.text, 'html.parser');

print('Menampilkan objek html')
print('======================')
print(obj)

print('\nMenampilkan title browser dengan tag')
print('======================================')
print(obj.title)

print('\nMenampilkan title browser tanpa tag')
print('======================================')
print(obj.title.text)

print('\nMenampilkan semua tag h2')
print('======================================')
print(obj.find_all('h2'));

print('\nMenampilkan semua teks h2')
print('======================================')
for headline in obj.find_all('h2'):
	print(headline.text)

print('\nMenampilkan headline berdasarkan div class')
print('============================================')
print(obj.find_all('div', class_='bungkus_txt_headline_center'))

print('\nMenampilkan semua teks headline')
print('============================================')
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
	print(headline.find('h2').text)

print('\nMenyimpan headline pada file text')
print('===================================')
f = (open('D:\\Kuliah\\Semester 2\\Proyek 1\\Pertemuan 6\\Scraping\\headline.txt', 'w'))
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
	f.write(headline.find('h2').text)
	f.write('\n')
f.close()

print('\nMenyimpan headline pada file json')
print('===================================')
#Import package json
import json;

# Deklarasi list kosong
data=[]

#Lokasi file json
f = (open('C:\\xampp2\\htdocs\\Scraping\\headline.json', 'w'))
for headline in obj.find_all('div', class_='bungkus_txt_headline_center'):
	data.append({"judul":headline.find('h2').text, "kategori":headline.find('h1').text})
jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()

from datetime import datetime
now = datetime.now()
tgl = now.strftime("%m/%d/%Y, %H:%M:%S")
dataTerkini=[]

f = (open('C:\\xampp2\\htdocs\\Scraping\\terkini.json', 'w'))
for terkini in obj.find_all('div', class_='teaser_conten1_center'):
	dataTerkini.append({"judul":terkini.find('h2').text, "kategori":terkini.find('h1').text, "tanggal":terkini.find('div',class_='date').text, "waktu":tgl})
jdumps = json.dumps(dataTerkini)
f.writelines(jdumps)
f.close()