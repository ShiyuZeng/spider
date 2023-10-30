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

terminate_flag = False  # 标志是否终止爬虫任务


def download_image(img_url, filename, count_var):
    try:
        urllib.request.urlretrieve(img_url, filename)
        count_var.set(count_var.get() + 1)  # 更新下载完成的照片数量
    except Exception as e:
        print(f"下载出错: {filename}, 错误信息: {e}")


def spider(urllist, count_var):
    global terminate_flag
    print("开始爬虫")
    count_var.set(0)  # 初始化下载完成的照片数量
    count = 1  # 照片计数
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in urllist:
            try:
                html = requests.get(url, headers=headers)
                soup = BeautifulSoup(html.text, 'html.parser')
                img_tags = soup.find_all('img')
                for imgtag in img_tags:
                    img_url = imgtag['src']
                    if img_url.startswith('https:'):
                        filename = f'F:\\Desktop\\2\\{count}.jpg'
                        future = executor.submit(download_image, img_url, filename, count_var)
                        futures.append(future)
                        count += 1
                    time.sleep(0.1)
                    if terminate_flag:  # 检查终止标志
                        break
                if terminate_flag:  # 检查终止标志
                    break
            except requests.RequestException as e:
                print(f"请求异常: {e}")
            except Exception as e:
                print(f"发生错误: {e}")

        # 等待所有下载任务完成
        for future in concurrent.futures.as_completed(futures):
            future.result()

    if terminate_flag:
        messagebox.showinfo("提示", "爬虫被终止")
    else:
        messagebox.showinfo("提示", "爬虫结束")


def start_spider(urls_entry, count_var):
    global terminate_flag
    terminate_flag = False
    urls = urls_entry.get("1.0", tk.END).strip().split('\n')
    spider(urls, count_var)


def terminate_spider():
    global terminate_flag
    terminate_flag = True


def create_ui():
    root = tk.Tk()
    root.title("图片爬虫")
    root.geometry("400x400")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    urls_label = tk.Label(frame, text="请输入要爬取的网址（每行一个）：")
    urls_label.pack()

    urls_entry = tk.Text(frame, height=6, width=30)
    urls_entry.pack()

    count_var = tk.IntVar()  # 用于记录下载完成的照片数量
    count_label = tk.Label(root, textvariable=count_var)
    count_label.pack()

    start_button = tk.Button(root, text="开始爬取", command=lambda: start_spider(urls_entry, count_var))
    start_button.pack(pady=10)

    terminate_button = tk.Button(root, text="终止爬虫", command=terminate_spider)
    terminate_button.pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    create_ui()