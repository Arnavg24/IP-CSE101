file = open('./q3.txt','r')
data=file.read()

data=data.split('...')
for i in range(len(data)):
    data[i]=data[i].split('\n')

for i in range(len(data)):
    for j in range(1,len(data[i])):
        data[i][j]=data[i][j].split(',')

for i in range(len(data)-1):
    data[i]=data[i][:len(data[i])-1]

for i in range(1,len(data)):
    data[i]=data[i][1:]
    data[i][0]=data[i][0][0]

data[-1].remove([''])

signs={}

for i in data:
    signs[i[0]]={}
    for record in i[1:]:
        signs[i[0]][record[0]]=int(record[1])
        

names=list(signs.keys())
for i in range(len(names)):
    names[i]=names[i].rstrip(':')

final=list(signs.values())

signs=[]
for i in range(len(final)):
    ans=final[i]
    summ=sum(final[i].values())
    signs.append(summ)

max_signs=max(signs)
min_signs=min(signs)

max_names=[]
min_names=[]

for i in range(len(signs)):
    if signs[i]==max_signs:
        max_names.append(names[i])
    if signs[i]==min_signs:
        min_names.append(names[i])

print('The most signed people is/are:',','.join(max_names))
print('The least signed people is/are:',','.join(min_names))
