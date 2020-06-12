# import requests
# r = requests.get("http://www.baidu.com")
# r.encoding = 'utf-8'
# print(r.text)






import requests
proxies = {
  'http':'http://127.0.0.1:8888',
  'https':'http://127.0.0.1:8888',
}
r = requests.get('http://www.baidu.com',proxies=proxies)
r.encoding = 'utf-8'
print(r.text)