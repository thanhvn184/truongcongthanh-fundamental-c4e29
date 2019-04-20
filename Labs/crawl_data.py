from urllib.request import urlopen
from bs4 import BeautifulSoup
# 1. Open connection
import pyexcel
from collections import OrderedDict
url = "https://dantri.com.vn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')


# with open("dantri.html", "wb") as f:
#     f.write(raw_data)



# 2. Find ROI (region of interest)


soup = BeautifulSoup(html_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew")


# 3. Extract ROI
list_dict =[]
li_list = ul.find_all("li")
for li in li_list:

    h4 = li.h4
    a = h4.a
    title = a.string.strip()
    link = url + a["href"]
    news = OrderedDict({
        "title": title,
        "link": link,
    })       
    list_dict.append(news)

pyexcel.save_as(records=list_dict, dest_file_name="dantri.xls")