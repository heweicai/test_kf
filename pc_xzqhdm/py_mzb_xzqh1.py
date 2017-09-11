# _*_ coding:utf-8 _*_
import requests
import re

url = "http://files2.mca.gov.cn/cws/201502/20150225155630452.htm"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
response = requests.get(url,headers = headers)


# 匹配所有非空字符
pat1 = r'<td.*>(\S+)<'
# pat1 = r'<td class.*>(\S+)</td>'

# 查询出所有匹配出的字符串结果
mydata  = re.findall(pat1,response.text)


# print(len(mydata))     取出下标的[1]到[6438]的数据

f = open("F:/mydata/年中华人民共和国县以上行政区划代码表.csv", 'w')


# 行政区划代码的数据处理
for i in range(0,len(mydata)-2):
    if ( i == 0 ):
         print ('行政区划代码', ',', '单位名称', file=f)

    if( (i % 2) == 1 and i>=2):
         print (mydata[i], ',', mydata[i+1], file=f)

f.close()