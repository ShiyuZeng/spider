import requests
from bs4 import *
from urllib import request
from lxml import etree
import urllib.request
import time


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
	    # "Referer": "",
}


# url = 'https://www.bizhizj.com/mntx/105294.html'
# html = requests.get(url,headers=headers)

# end = etree.HTML(html.text)
# img_tags = end.xpath('//div[@class="neirong_left_tx"]/img')
# print(img_tags)

# i = 11
# for imgtag in img_tags:
#     imgurl = imgtag.xpath('./@src')[0]
#     i = i + 1
#     data = (imgurl,
#             headers) 
#     request.urlretrieve(imgurl,r'F:\\Desktop\\1\\'+str(i)+'.jpg') 
#     # img = requests.get(imgurl, headers)
#     # path = 'F:\\Desktop\\1\\'+str(i)+'.jpg'
#     # with open(path,"wb") as f:
#     #     f.write(img.content)
#     # f.closed
#     print ("download compelete")  
#     time.sleep(0.1)
def main():
	resource = []
	while True:
		webadd = input("Please input some wed addresses to start, input -1 as finish：")
		if webadd == str(-1):
			print("you input a -1,so inputing is over")
			break
		resource.append(webadd)
	spider(resource)
	return 0 

def spider(urllist):
	print ("start spider")
	for url in urllist:
		html = requests.get(url,headers=headers)
		end = etree.HTML(html.text)
		img_tags = end.xpath('//div[@class="neirong_left_tx"]/img')
		print(img_tags)
	# i = 0
	# for imgtag in img_tags:
	# 	imgurl = imgtag.xpath('./@src')[0]
	# 	i = i + 1
	# 	request.urlretrieve(imgurl,r'F:\\Desktop\\1\\'+str(i)+'.jpg')
	# 	print ("download compelete")  
	# 	time.sleep(0.1) 
	return 0



main()