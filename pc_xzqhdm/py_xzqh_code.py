__author__ = 'HeWeiCai'
# _*_ coding:utf-8 _*_

# 注释掉了所有内容，以另一种方式写循环程序

import requests

url = "http://www.mca.gov.cn/article/sj/tjbz/a/2017/201707/201708241435.html"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
response = requests.get(url, headers = headers)

data = response.content

with open("F:/mydata/2017年中华人民共和国县以上行政区划变更情况源代码测试.txt", 'wb') as f:
    f.write(data)