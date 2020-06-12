

#用户接口

import requests

#请求头
header = {'Content-Type':'application/x-www-form-urlencoded'}

payload = {'username':'auto','password':'sdfsdfsdf'}
r = requests.post('http://127.0.0.1/api/mgr/loginReq',headers = header,data=payload)

print(r.text)