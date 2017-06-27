#coding=UTF-8
import facebook, json, pyprind

token='EAACEdEose0cBAJ4k8OC3WQblAb0LjdGNby5JxY4LHgZCm0SJLunElknjfZB5n9Ae2SzayvOKlskUZBPbwi045nEVR8wg50SmpaW4TuzEk7ZBlthwasZBmYfJALRqLBQpXlUO3RFJwwtajRfhnaOkNqxAyMGA78KRNYbYi5CZCELN7E3usLaeOZCaWl7lv2vJEcZD'
#token為access token
graph=facebook.GraphAPI(access_token=token, version='2.6')

#i為要所需的FB頁面之id
def crawl(i):
	info = graph.get_object(i)
	print(info)
	posts = graph.get_connections(i, 'posts')
	for p in pyprind.prog_bar(posts['data']):
		p['reactions'] = graph.get_connections(p['id'], 'reactions')
		p['comments'] = graph.get_connections(p['id'], 'comments')
	json.dump(posts, open('facebook.json', 'w'))

crawl('1623149734611090')#電影筆記