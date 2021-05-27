import os
import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

def get_href(headers):
    response = requests.get('http://uscarriers.net/sitemap.html' , headers=headers)
    soup = BeautifulSoup(response.content,'lxml')
    href = []
    if os.path.exists('./href.txt'):
        os.remove('./href.txt')
    for item in soup.find_all(name="li"):
        href.append(item.a.attrs['href'])
        with open('href.txt','a+') as f :
            f.write(item.a.attrs['href'] + '\n')

def get_now_date(url):
    try:
        res = requests.head(url)
        data = res.headers['Last-Modified'].split(',')[1].strip()
    except:
        data = 'None'
    return data

#get_href(headers)
def last_date(url):
    data = 'None'
    with open("memo.txt",'r') as f :
        for line in f.readlines():
            pre = line.strip().replace('\n','').split('##')
            if url == pre[0] :
                try:
                    data = pre[1].split(',')[1].strip()
                except:
                    return data
            else:
                continue
    return data

def updateFile(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

with open('href.txt','r') as f :
    for item in f.readlines():
        url = item.strip().replace('\n','')
        last_data = last_date(url)
        now_data = get_now_date(url)
        print(url + "最新更新时间" + now_data)

        flag = True

        if last_data != 'None' and now_data!= 'None':
            last = last_data.split(' ')
            now = now_data.split(' ')
            for i in range(len(last)):
                if last[i] != now[i]:
                    flag = False
        else:
            flag = False

        if flag == True  :
            print(url + "无需更新")
            continue
        else:
            updateFile('memo.txt',last_data,now_data)
            print(url + "备忘录时间信息已更新！")
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'lxml')
                try:
                    title = soup.find(name="title").string
                    content = []
                    for p in soup.find_all(name='p'):
                        for item in p.contents:
                            if item.string:
                                content.append(item)
                            else:
                                content.append(item)
                    print(content)
                    now = time.strftime("%Y-%m-%d",time.localtime())
                    with open(str(now) + ".txt", 'a+', encoding='utf-8') as file:
                        file.write(url + '\n')
                        file.write(title + '\n')
                        for line in content:
                            file.write(str(line) + '\n')
                        file.write(
                            "------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                except:
                    continue
            else:
                print('connecting' + url + "error")
                continue
















