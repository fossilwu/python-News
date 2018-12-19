


from bs4 import BeautifulSoup
import requests

import urllib
from bs4 import BeautifulSoup

url = 'http://www.baidu.com/s'
values = {'wd': 'wang'}
encoded_param = urllib.parse.urlencode(values)
full_url = url + '?' + encoded_param
response = urllib.parse.urlopen(full_url)
soup = BeautifulSoup(response)
soup.find_all('a')
