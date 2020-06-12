import requests

head = {'Content-Type':'application/json'}
payload = {
'action':'add_course_json','data':{
  "name":"初中化学",
  "desc":"初中化学课程",
  "display_idx":"4"
}
}

proxies = {
  'http':'http://127.0.0.1:8888',
  'https':'http://127.0.0.1:8888',
}
r = requests.post('http://127.0.0.1/apijson/mgr/sq_mgr/',headers = head,json=payload,proxies=proxies)

print(r.text)