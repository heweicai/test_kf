# _*_ coding:utf-8 _*_
import requests
import re

url = "http://www.mca.gov.cn/article/sj/tjbz/a/201713/201708040959.html"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
response = requests.get(url, headers = headers)


data = re.findall('(\d{6})(\D+)',''.join(re.findall('>(\w+)\s*<', response.text)))

f = open("F:/mydata/1980年中华人民共和国县以上行政区划代码表.csv", 'w')
print('行政区划代码', ',', '单位名称', file=f)
for i in range(0, len(data)):
   print (data[i][0], ',', data[i][1], file=f)

f.close()


"""
# 正则表达匹配所有非空字符
pat1 = r'<td.*>(\S+)<'
# pat1 = r'<td class.*>(.+)</td>'
# pat1 = r'<td class.*>(\S+)</td>

# 查询出所有匹配出的字符串结果
mydata  = re.findall(pat1, response.text)

print(mydata)

"""