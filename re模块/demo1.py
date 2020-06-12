
import re

str1 = 'yemYeng'
res = re.findall('ye',str1,re.I)#re.I不区分大小写
print(res)

#re.S---让 . 包含 换行符
str2 = 'songqinSo\n'
res = re.findall('so.',str2,re.I|re.S)
print(res)