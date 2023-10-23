import random
w = open('sample.tsv','w')
f2 =open("train_sample.tsv")
f3=open("test_sample.tsv")

l=[]
ll=[]
for i in f2:
    l.append(i.strip('\n'))
    ll.append(i.split('\t')[1])

ss = [i.strip('\n').split('	')[1] for i in f3]
rel_set=[]
lines =f.readlines()
random.shuffle(lines)
print(lines[0])
for line in lines:
    head,rel,tail=line.strip('\n').split('\t')
    # print(rel)
    if rel not in rel_set:
        rel_set.append(rel)
        s=ss[ll.index(rel)].split('	')[-1]
        sh=l[ll.index(rel)].split('\t')[0]
        w.write(line)
        w.write(
            f'predict the tail entity [MASK] from the given ({head}, {rel}, [MASK]) by completing the sentence \"{s}\".The answer is {tail}.\n'
        )
        w.write(
            f'predict the tail entity [MASK] from the given ({sh}, {rel}, [MASK]) by completing the sentence \"{s}\".The answer is \n'
        )

print(len(rel_set))


