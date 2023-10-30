import csv
import requests
import os
import string
from urllib.parse import quote
from fpdf import FPDF

def sanitize_filename(filename):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_filename = ''.join(c for c in filename if c in valid_chars)
    return sanitized_filename

def download_images_from_csv(csv_file, output_dir):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过标题行
        count = 1  # 初始化计数器
        filenames = []  # 存储下载的文件名
        for row in reader:
            image_url = row[0]  # 假设图片URL在第一列

            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                filename = os.path.join(output_dir, f"{count}.png")  # 使用计数器作为文件名
                with open(filename, 'wb') as image_file:
                    for chunk in response.iter_content(1024):
                        image_file.write(chunk)
                print(f"已下载并保存图片：{filename}")
                count += 1  # 计数器加1
                filenames.append(filename)  # 将文件名添加到列表中
            else:
                print(f"无法下载图片：{image_url}")

        # 生成 PDF 文件
        pdf = FPDF()
        for filename in sorted(filenames):  # 按文件名升序排列
            pdf.add_page()
            pdf.image(filename, x=10, y=10, w=190)  # 将图片添加到 PDF 页面上

        pdf.output(os.path.join(output_dir, "images.pdf"), "F")  # 保存 PDF 文件

# 设置 CSV 文件路径和输出目录
csv_file = 'C:/Users/Zeng/Downloads/urls.csv'
output_dir = 'F:/Desktop/1/'

# 创建输出目录（如果不存在）
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 下载图片并生成 PDF
download_images_from_csv(csv_file, output_dir)