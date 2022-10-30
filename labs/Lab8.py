from distutils.spawn import spawn
from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://lego.com/en-us/themes/star-wars').content
soup = BeautifulSoup(r, 'html.parser')
h2 = soup.find('h2', {"class":"Text__BaseText-sc-13i1y3k-0 iSNFVS ProductLeafSharedstyles__Title-sc-1yg7ucv-9 zimKm"})
title = h2.text
span = soup.find('span', {"class":"Text__BaseText-sc-13i1y3k-0 eTDhBg ProductPricestyles__StyledText-sc-vmt0i4-0 tMWye"})
price = span.text
print("The price of the lego %s is listed at %s " % (title, price))
