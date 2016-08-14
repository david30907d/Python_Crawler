import requests, json, jieba, operator, sys
token = 'EAACEdEose0cBAPbbADOk9htDE38ZBzd1x1P9k6BTIOcf3f1ZA35bSCGP1maWESrLauuNFjs9LuVlJwKuZBgcJFeMGE7dr8CmhZAILBE6ZCz0ie8M68ZARnpA2Ju6JvnrVGNZANoeFMBTi7470VP8O2ii2ZCwvZBnekBPiX0DBqk4ETgZDZD'
re = requests.get('https://graph.facebook.com/v2.5/me/posts?since=1420041600&limit=100&access_token=' + token)
#if you want to chose a specific time span, append 'since=1420041600' after 'post?' 
#cause it use Unix seconds, so 1420041600 means 2015/01/01
jo=json.loads(re.text)
count=0
corpus = []
while 'paging' in jo:
	for i in jo['data']:
		if 'message' in i and 'story' in i:
			corpus+=jieba.cut(i['message'])
		elif 'message' in i:
			corpus+=jieba.cut(i['message'])	
		count+=1		
	re = requests.get(jo['paging']['next'])
	jo=json.loads(re.text)

print('total %d posts' % count)

dic = {}
for i in corpus:
	if i not in dic :
		dic[i] = 1
	else :
		dic[i] +=1
sorted_word = sorted(dic.items(), key = operator.itemgetter(1), reverse = True)

fname = sys.argv[1]
pname = sys.argv[2]
with open(fname, 'a', encoding='UTF-8') as f:
	count=0
	f.write('\n'+pname+'`s analysis : '+'\n')
	for i in sorted_word:
		if len(i[0]) >= 2:
			print(i[0],i[1])
			f.write(str(count+1)+' :'+str(i)+'\n')
			count+=1
		if count >= 30 :
			break