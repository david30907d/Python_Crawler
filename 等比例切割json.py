import json, sys

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    n = int(n)
    for i in range(0, len(l), int(len(l)/n)):
        yield l[i:i + int(len(l)/n)]

j = json.load(open(sys.argv[1], 'r'))
for index, i in enumerate(chunks(j, sys.argv[2])):
	json.dump(i, open('{}.json'.format(index), 'w'))