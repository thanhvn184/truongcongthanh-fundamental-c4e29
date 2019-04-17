from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
soup = BeautifulSoup(raw_data,"html.parser")
section = soup.find('section','section chart-grid')
li_list = section.find_all('li')
result =[]
title_list = []
for li in li_list:
    h3 = li.h3
    a1 = h3.a
    h4 = li.h4
    a2 = h4.a
    title = a1.string.strip()
    band = a2.string.strip()
    Title_list.append(title)
    Final_list = OrderedDict({"Title":title,"Band":band})
    Result.append(Final_list)

pyexcel.save_as(records=result, dest_file_name="iTunes.xlsx")
# for i in Title_list:
#     options = {
#         'default_search': 'ytsearch', 
#         'max_downloads': 1,
#         'format': 'bestaudio/audio'
#     }
#     dl = YoutubeDL(options)
#     dl.download([i])