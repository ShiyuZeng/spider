import requests
from bs4 import *
from urllib import request
from lxml import etree
import urllib.request
import time


headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
	     "Connection": "keep-alive",
		"Cookie": "__yjs_duid=1_58c2582ae93bb444e72c7182680281b51671871882633",
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
	i = 125
	for url in urllist:
		html = requests.get(url,headers=headers)
		soup = BeautifulSoup(html.text, 'html.parser')
		img_tags = soup.find_all('img')
		for imgtag in img_tags:
			imgurl = imgtag['src']
			i = i + 1
			if imgurl.startswith('https:'):
				request.urlretrieve(imgurl,r'F:\\Desktop\\2\\'+str(i)+'.jpg')
				print ("download compelete")
				if i % 24 == 0:
					break
				elif i % 37 == 0:
					break
				elif i % 63 == 0:
					break
				elif i % 88 == 0:
					break
				elif i % 126 == 0:
					break
				elif i % 135 == 0:
					break
			else:
				continue
			time.sleep(0.1)
	return 0

main()


# 测试网站：

# https://www.bizhizj.com/nstx/128920.html
# https://www.bizhizj.com/nstx/128914.html
# https://www.bizhizj.com/nstx/128506.html
# https://www.bizhizj.com/mntx/107859.html
# https://www.bizhizj.com/mntx/106088.html
# https://www.bizhizj.com/mntx/105299.html
# https://www.bizhizj.com/mntx/71113.html
# https://www.bizhizj.com/mntx/71145.html
# https://www.bizhizj.com/mntx/71145.html
# https://www.bizhizj.com/mntx/71123.html
# https://www.bizhizj.com/mntx/68480.html
# https://www.bizhizj.com/mntx/6551.html
# https://www.bizhizj.com/mntx/115434.html
# https://www.bizhizj.com/mntx/117852.html
# -1



# https://www.bizhizj.com/mxtx/116771.html
# https://www.bizhizj.com/mxtx/116769.html
# https://www.bizhizj.com/mxtx/126219.html
# https://www.bizhizj.com/mxtx/126213.html
# https://www.bizhizj.com/mxtx/126213.html
# https://www.bizhizj.com/mxtx/103295.html
# https://www.bizhizj.com/mxtx/101795.html
# https://www.bizhizj.com/mxtx/96553.html
# https://www.bizhizj.com/mxtx/53549.html
# https://www.bizhizj.com/mxtx/53286.html
# -1
