'''
Created on 2017年10月19日

@author: Administrator
'''
import re
from bs4 import BeautifulSoup  
from urllib import request
import time


if __name__ == "__main__":
    url = 'https://www.igxe.cn/product-116228012'
    proxys = [{'http': '113.128.29.31:43319'}, {'http': '171.38.197.112:8123'}, {'http': '101.64.103.251:9999'}, {'http': '119.162.211.8:8118'}, {'http': '49.89.77.225:20853'}, {'http': '110.73.41.36:8123'}, {'http': '220.165.176.27:9999'}, {'http': '122.4.163.0:808'}, {'http': '221.227.250.46:8888'}, {'http': '218.56.200.156:8118'}, {'http': '182.246.219.246:80'}, {'http': '49.87.146.217:29126'}, {'http': '110.73.54.1:8123'}, {'http': '27.18.131.209:808'}, {'http': '222.76.144.133:35610'}, {'http': '183.19.211.15:808'}, {'http': '125.113.252.185:41030'}, {'http': '110.73.9.147:8123'}, {'http': '113.120.63.235:21108'}, {'http': '115.203.181.125:42413'}, {'http': '183.133.78.32:8118'}, {'http': '110.72.19.194:8123'}, {'http': '111.78.172.92:22467'}, {'http': '120.40.134.218:27540'}, {'http': '110.73.7.159:8123'}, {'http': '121.31.100.95:8123'}, {'http': '125.109.199.228:29868'}, {'http': '111.155.116.220:8123'}, {'http': '222.85.22.21:808'}, {'http': '36.35.127.240:9999'}, {'http': '123.55.178.146:41995'}, {'http': '122.4.28.27:37393'}, {'http': '117.86.205.91:8888'}, {'http': '110.73.7.202:8123'}, {'http': '123.55.185.48:25365'}, {'http': '125.125.214.128:10000'}, {'http': '116.25.14.173:8118'}, {'http': '49.87.146.96:45340'}, {'http': '114.239.249.172:23344'}, {'http': '182.88.164.56:8123'}, {'http': '110.72.43.46:8123'}, {'http': '119.55.116.118:9999'}, {'http': '110.73.0.56:8123'}, {'http': '115.213.200.146:808'}, {'http': '218.73.138.161:40722'}, {'http': '113.121.180.166:808'}, {'http': '182.88.254.109:8123'}, {'http': '124.72.96.138:22766'}, {'http': '121.204.165.176:8118'}, {'http': '171.39.28.113:8123'}, {'http': '113.4.196.75:9999'}, {'http': '122.4.29.200:47088'}, {'http': '218.81.135.138:28796'}, {'http': '101.65.42.153:9999'}, {'http': '182.34.16.88:28444'}, {'http': '125.122.19.168:22500'}, {'http': '125.211.202.26:53281'}, {'http': '115.226.15.249:1080'}, {'http': '60.169.216.147:41858'}, {'http': '222.93.230.11:8118'}, {'http': '114.115.216.99:80'}, {'http': '121.206.84.177:48948'}, {'http': '121.31.197.34:8123'}, {'http': '42.242.151.65:9999'}, {'http': '110.73.1.162:8123'}, {'http': '27.150.87.86:34339'}, {'http': '175.19.42.253:8080'}, {'http': '49.77.211.53:40712'}, {'http': '49.85.5.251:27532'}, {'http': '218.108.215.36:80'}, {'http': '120.40.38.132:808'}, {'http': '111.155.120.178:8123'}, {'http': '110.72.16.172:8123'}, {'http': '219.132.25.105:808'}, {'http': '120.78.15.63:80'}, {'http': '36.35.48.206:9999'}]
    for ip in proxys:
        proxy_support = request.ProxyHandler(ip)
        opener = request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')]
        request.install_opener(opener)
        response = request.urlopen(url)
        html = response.read().decode("utf-8")
        bf = BeautifulSoup(html, 'lxml')
        item_attr = bf.find(class_='mod-equipmentDetail-bd com-out').find('h3').get_text()
        print(str(ip)+item_attr)
        time.sleep(1)