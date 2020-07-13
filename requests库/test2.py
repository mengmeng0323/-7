
#教管系统--列出课程

# payload只支持字典和字符串

import requests
payload = {'action':'list_course','pagenum':'1','pagesize':'20'}
proxies = {
  'http':'http://127.0.0.1:8888',
  'https':'http://127.0.0.1:8888',
}
r = requests.get("http://127.0.0.1/api/mgr/sq_mgr/",params=payload,proxies=proxies)
print(r.text)




import requests
