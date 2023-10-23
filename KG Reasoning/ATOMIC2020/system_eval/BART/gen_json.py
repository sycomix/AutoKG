import json
f =open("example.tsv")
fw=open("1_CHATGPT.json",'w')
for it in f:
    i=it.strip().split('\t')
    print(i)
    js = {'head': i[0], 'relation': i[1], 'tails': i[2].split('    ')[0]}
    js['generations'] = list(i[2].split('    ')[1].split(','))
    js['greedy']=i[2].split('    ')[1].split(',')[0]
    fw.write(json.dumps(js)+'\n')