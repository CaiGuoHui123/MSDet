import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

items = []  # 创建空列表，拟存储考研调剂信息
# 截至2022年2月25日，该网站公布的2022年考研调剂信息仅7页。
for i in range(1, 501):
    url = f'http://www.chinakaoyan.com/tiaoji/schoollist/pagenum/{i}.shtml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56'}
    try:
        # 发起请求
        r = requests.get(url, headers=headers, timeout=5)
    except Exception:
        # 若请求失败，则等待3秒，等待浏览器加载，再请求一次
        time.sleep(3)
        r = requests.get(url, headers=headers, timeout=5)
        # 解析网页
    soup = BeautifulSoup(r.text, 'html.parser')
    # 获取所有信息
    data = soup.find_all('div', class_='info-item font14')
    for i in data:
        school = i.find('span', class_='school').text  # 获取学校
        name = i.find('span', class_='name').text  # 获取专业
        title = i.find('span', class_='title').text  # 获取标题
        url = 'https://www.chinakaoyan.com' + i.find('span', class_='title').find('a')['href']  # 获取url地址
        time = i.find('span', class_='time').text  # 获取时间
        item = [school, name, title, time, url]
        items.append(item)
# 保存信息
df = pd.DataFrame(items, columns=['学校', '专业', '调剂标题', '发布时间', '网址'])
df.to_excel(r'中国考研网2022调剂信息截至20220308.xlsx')