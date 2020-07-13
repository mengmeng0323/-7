
# 教管系统--新增课程

import requests

header = {'Content-Type':'application/x-www-form-urlencoded'}
payload = {'action':'add_course','data':'''{
  "name":"初中化学",
  "desc":"初中化学课程",
  "display_idx":"4"
}'''}

r=requests.post('http://127.0.0.1/api/mgr/sq_mgr/',headers= header,data=payload)
