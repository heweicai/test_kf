__author__ = 'HeWeiCai'
# _*_ coding:utf-8 _*_

# 注释掉了所有内容，以另一种方式写循环程序
"""
import requests

url = "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708040959.html"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
response = requests.get(url, headers = headers)

data = response.content

with open("F:/mydata/source_dm/1980年中华人民共和国县以上行政区划源代码.html", 'wb') as f:
    f.write(data)

"""


# 以另一种方式写循环下载多个html文件，并保存到多个文件中
import requests
import re

url = "http://www.mca.gov.cn/article/sj/tjbz/a/2017/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
response1 = requests.get(url, headers= headers)

data1 = response1.text

pat1 = r'</td><td class="arlisttd"><a class="artitlelist" href="(\S+)" target="_blank"'

mydata = re.findall(pat1, data1)

"""

# 拼成完整的url,采用两个数组方式拼接
head_url = ['http://www.mca.gov.cn']*len(mydata)
if(len(head_url)==len(mydata)):
    my_url = []
    for i in range(0, len(head_url)):
        my_url+= [head_url[i] + mydata[i]]
else:
    my_url= '统一资源定位符url为空'

print(my_url)


# 拼成完整的url,采用两个数组方式拼接
head_url = ['http://www.mca.gov.cn']*len(mydata)
if(len(head_url)==len(mydata)):
    my_url = []
    for i in range(0, len(head_url)):
        my_url.append([head_url[i] + mydata[i]])
else:
    my_url= '统一资源定位符url为空'

print(my_url)


"""

# 采用一个字符串与一个数组拼接
head_url1 ='http://www.mca.gov.cn'
my_url1 = []
my_url1 = [head_url1 + mydata[j] for j in range(0, len(mydata))]
print(my_url1)



"""

# 在requests.get(a + b[i])进行拼接
head_url1 ='http://www.mca.gov.cn'
for k in range(0, len(mydata)):
    if(k%2 == 1):
        response2 = requests.get(head_url1+mydata[k], headers= headers)
print(response2.text)

"""