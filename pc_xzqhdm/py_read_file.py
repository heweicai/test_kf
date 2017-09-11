__author__ = 'HeWeiCai'
# _*_ coding:utf-8 _*_

#import re

path = 'F:/mydata/2017年中华人民共和国县以上行政区划变更情况源代码.txt'

with open(path, 'rt') as f:
    data = f.read()
# pat1 = r'\<td.*>(\S+)</td>'
#data1 = re.findall(pat1, data)
#print (data1)


print(data);