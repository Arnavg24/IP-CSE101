f= open("./q7.txt", "r")
addrbook=eval(f.read())
f.close()

file= open("./q7_merge.txt", "r")
addrbook_2=eval(file.read())
file.close()

names=list(addrbook_2.keys())
for name in names:
    if name in list(addrbook.keys()):
        addrbook[name].append(addrbook_2[name])
    else:
        addrbook[name]=addrbook_2[name]

print(addrbook)

with open('q7_bonus_answer.txt','w') as file :
    file.write(str(addrbook))

