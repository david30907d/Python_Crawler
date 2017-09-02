import requests
s = requests.session()
login = {
"account":"4102031025",
"pwd":"as23cgsh",
"login":"登入"
}
s.post("http://rent.sim.nchu.edu.tw/index.php", login)
data = {
  "queryPlace": "網球場",
  "date": "2017/09/12"
}
res = s.post("http://rent.sim.nchu.edu.tw/index.php?module=rent_pro", data=data)
with open('test.html', 'w') as f:
    f.write(res.text)