import tkinter as tk
from tkinter import messagebox
import concurrent.futures
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


def download_image(img_url, filename):
    try:
        urllib.request.urlretrieve(img_url, filename)
        print(f"下载完成: {filename}")
    except Exception as e:
        print(f"下载出错: {filename}, 错误信息: {e}")


def spider(urllist):
    print("开始爬虫")
    i = 125
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in urllist:
            try:
                html = requests.get(url, headers=headers)
                soup = BeautifulSoup(html.text, 'html.parser')
                img_tags = soup.find_all('img')
                for imgtag in img_tags:
                    img_url = imgtag['src']
                    i += 1
                    if img_url.startswith('https:'):
                        filename = f'F:\\Desktop\\2\\{i}.jpg'
                        future = executor.submit(download_image, img_url, filename)
                        futures.append(future)
                        if i % 24 == 0 or i % 37 == 0 or i % 63 == 0 or i % 88 == 0 or i % 126 == 0 or i % 135 == 0:
                            break
                    time.sleep(0.1)
            except requests.RequestException as e:
                print(f"请求异常: {e}")
            except Exception as e:
                print(f"发生错误: {e}")

        # 等待所有下载任务完成
        for future in concurrent.futures.as_completed(futures):
            future.result()

    messagebox.showinfo("提示", "爬虫结束")


def start_spider(urls_entry):
    urls = urls_entry.get("1.0", tk.END).strip().split('\n')
    spider(urls)


def create_ui():
    root = tk.Tk()
    root.title("图片爬虫")
    root.geometry("400x300")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    urls_label = tk.Label(frame, text="请输入要爬取的网址（每行一个）：")
    urls_label.pack()

    urls_entry = tk.Text(frame, height=6, width=30)
    urls_entry.pack()

    start_button = tk.Button(root, text="开始爬取", command=lambda: start_spider(urls_entry))
    start_button.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    create_ui()