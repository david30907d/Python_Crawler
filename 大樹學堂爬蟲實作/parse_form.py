import requests, re, json
res = requests.get('http://www.oanda.com/currency/historical-rates/')
result = re.search('("data":\[\[.*\]\])',res.text)
result = '{'+result.group(1)+'}'
json_data = json.loads(result)
print(json_data)
