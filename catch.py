# coding=utf-8
import urllib
from bs4 import BeautifulSoup

url ='http://www.baidu.com/s'
values ={'wd':'网球'}
encoded_param = urllib.urlencode(values)
full_url = url +'?'+ encoded_param
response = urllib.urlopen(full_url)
soup =BeautifulSoup(response)
alinks = soup.find_all('a')