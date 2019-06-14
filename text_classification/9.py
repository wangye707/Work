import requests
import time
import pymysql
import random
from multiprocessing import Pool

#通过pymysql链接mysql
conn = pymysql.connect(host = '127.0.0.1' , port = 3306 , user = 'root' , passwd = '123456')
cur = conn.cursor()
result = []
video_list = []

#加载User_Agent函数
def LoadUserAgent(uafile):
    uas = []
    with open(uafile,'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1])
    random.shuffle(uas)
    return uas

#加载user_agents.txt文件
uas = LoadUserAgent("user_agents.txt")

def getHtmlInfo(url):
    #随机选择user_agent
    ua = random.choice(uas)
    #加载headers
    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'api.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        # 'Referer': 'https://www.bilibili.com/video/' + str(i) + '?spm_id_from=333.338.recommend_report.3',
        'User-Agent': ua
    }
    # 通过requests.get来请求数据，再通过json()解析
    response = requests.get(url, headers=headers, timeout=6).json()
    try:
        data = response['data']
        video = (
            data['aid'], data['view'], data['danmaku'],
            data['reply'], data['favorite'], data['coin'], data['share'])
        video_list.append(video)
        print(video_list)
        save_db()
        # time.sleep(0.4)
    except:
        print('-----')


# 将数据保存至mysql
def save_db():
    global video_list, cur, conn
    sql = "insert into bili_video values(%s, %s, %s, %s, %s, %s, %s);"
    for row in video_list:
        try:
            # print(row)
            cur.execute(sql, row)
        except:
            conn.rollback()
    conn.commit()
    video_list = []

if __name__ == '__main__':
    for i in range(10, 2000):
        pool = Pool(10)
        begin = (i-1)*10000
        urls = ['https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(j) for j in range(begin, begin+10000)]
        try:
            pool.map(getHtmlInfo, urls)
        except:
            print("错误")
            pool.close()
            pool.join()
            time.sleep(0.2)
            pool = Pool(10)
            pool.map(getHtmlInfo, urls)

    conn.close()


    # 加载代理IP函数
    def LoadProxies(ipfile):
        ips = []
        with open(ipfile, 'r') as ipf:
            for ip in ipf.readlines():
                if ip:
                 ipf.append(uas.strip())
        # 随机打乱列表
        random.shuffle(ips)
        return ips


    # 加载proxies.txt文件
    ips = LoadProxies("proxies.txt")


    def getHtmlInfo(url):
        # 随机选择user_agent
        ua = random.choice(uas)
        ip = random.choice(ips)
        # 加载headers
        headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
            'Connection': 'keep-alive',
            'Host': 'api.bilibili.com',
            'Origin': 'https://www.bilibili.com',
            # 'Referer': 'https://www.bilibili.com/video/' + str(i) + '?spm_id_from=333.338.recommend_report.3',
            'User-Agent': ua
        }
        # 通过requests.get来请求数据，再通过json()解析
        response = requests.get(url, headers=headers, timeout=6, proxies={'https': 'https://' + ip}).json()
        try:
            data = response['data']
            video = (
                data['aid'], data['view'], data['danmaku'],
                data['reply'], data['favorite'], data['coin'], data['share'])
            video_list.append(video)
            print(video_list)
            save_db()
            # time.sleep(0.4)
        except:
            print('-----')
            import pandas as pd
            import numpy as np
            import matplotlib.pyplot as plt
            # % matplotlib inline

            filename = 'bili_video.csv'
            data = pd.read_csv(filename)
            data = data.drop(data[data.view == -1].index, axis=0)
            data.describe()



            ''';
            fuck yuan ge fuckdhaskhdkasnxkasnakcjsajc122353546564654kjo;pl'ojiuguyygiuh566757887908jkjhb/
            
            '''