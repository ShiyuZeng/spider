import requests
from bs4 import BeautifulSoup
import urllib.request
import time

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Connection": "keep-alive",
    "Cookie": "__yjs_duid=1_58c2582ae93bb444e72c7182680281b51671871882633",
}


def spider(urllist):
    print("开始爬虫")
    i = 125
    for url in urllist:
        try:
            html = requests.get(url, headers=headers)
            soup = BeautifulSoup(html.text, 'html.parser')
            img_tags = soup.find_all('img')
            for imgtag in img_tags:
                imgurl = imgtag['src']
                i += 1
                if imgurl.startswith('https:'):
                    urllib.request.urlretrieve(imgurl, f'F:\\Desktop\\2\\{i}.jpg')
                    print("下载完成")
                    if i % 24 == 0 or i % 37 == 0 or i % 63 == 0 or i % 88 == 0 or i % 126 == 0 or i % 135 == 0:
                        break
                time.sleep(0.1)
        except requests.RequestException as e:
            print(f"请求异常: {e}")
        except Exception as e:
            print(f"发生错误: {e}")
    print("爬虫结束")


def main():
    resources = []
    while True:
        webadd = input("请输入要爬取的网址，输入-1结束：")
        if webadd == str(-1):
            print("输入-1，爬取结束")
            break
        resources.append(webadd)
    spider(resources)


if __name__ == '__main__':
    main()