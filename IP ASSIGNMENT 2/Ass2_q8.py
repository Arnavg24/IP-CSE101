f=open("q8.txt", "r").read()
def parseline(line):

    url=line[:line.find(",")]
    line = line[line.find(",")+1:]
    i_imp=line[:line.find(":")]
    desc=line[line.find(":")+1:]
    
    return url, i_imp, desc
lines=f.split("\n")
dictionary={}
ids=[]
for line in lines:
    urlid,i_imp,desc=parseline(line)
    dictionary[urlid]={}
    ids.append(urlid)

for line in lines:
    urlid,i_imp,desc=parseline(line)
    list_id=[]
    for id in ids:
        if(id in desc):
            list_id.append(id)
    dictionary[urlid]['init_imp']=float(i_imp)
    dictionary[urlid]['urls_access']=list_id

for url in dictionary:
    overall_imp=0
    for url2 in dictionary:
        if(url!=url2):
            if(url in dictionary[url2]['urls_access']):
                overall_imp+=(dictionary[url2]['init_imp']/len(dictionary[url2]['urls_access']))
    dictionary[url]['overall_imp']=overall_imp

l1=[]

for url in dictionary:
    l1.append((dictionary[url]['overall_imp'], url))

l1=sorted(l1, reverse=True)
N=int(input("Enter N: "))
l1=l1[:N]

for url_tup in l1:
    print(f"{url_tup[1]}, Overall Importance: {round(url_tup[0],2)}")