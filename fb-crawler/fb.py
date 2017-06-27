#coding=UTF-8
import facebook, json, pyprind

token=''
#token為access token
graph=facebook.GraphAPI(access_token=token, version='2.6')

#i為要所需的FB頁面之id
def crawl(i):
	info = graph.get_object(i)
	posts = graph.get_connections(info['id'], 'posts')
	for p in pyprind.prog_bar(posts['data']):
		p['reactions'] = graph.get_connections(p['id'], 'reactions')
		p['comments'] = graph.get_connections(p['id'], 'comments')
	json.dump(posts, open('facebook.json', 'w'))

crawl('1623149734611090')#電影筆記