import requests
from lxml import etree 
from urllib import request
from bs4 import *

url = 'http://www.win4000.com/mobile.html'
feedback =  requests.get(url)

soup = BeautifulSoup(feedback.text, 'html.parser')

imgtags = soup.find_all('img')

print(imgtags)

i = 1
for imgtag in imgtags:
    imgurl = imgtag['src']
    request.urlretrieve(imgurl,r'F:\\Desktop\\1\\'+str(i)+'.png') 
    i = i+1
    print ("download compelete")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    