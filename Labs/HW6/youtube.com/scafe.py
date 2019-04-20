from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn?fbclid=IwAR3o4brXwbbkdz6DlcWtrBAPv1DlDBRH-0NX2FRtf-SZoe0dnG7ps_yJaWA"
conn = urlopen(url)
raw_data = conn.read()
print(raw_data)
html_content = raw_data.decode('utf8')
print(html_content)