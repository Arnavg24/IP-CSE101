n=int(input("Please enter number of coordinates:"))
#taking number of coordinates so that can loop over them
l=[]
for i in range(n):   
    x,y = list(map(int,input("enter x y (respectively):").split()))
    l.append((x,y))

l_ans=[]
for i in range(n):
    l_new=[]
    for j in range(3):
      l_new.append(1)  
    l_ans.append(l_new)

for i in range(len(l_ans)):
    l_ans[i] = [l[i][0], l[i][1], 1]

cx=int(input('enter value of cx:'))
cy=int(input('enter value of cy:'))
multiplier=[[cx,0,0],[0,cy,0],[0,0,1]]


final = []
for i in range(len(l_ans)):
    temp = [0 for b in range(3)]
    for j in range(3):
        for k in range(3):
            temp[j] += l_ans[i][k] * multiplier[k][j]
    final.append(temp)
print('respective values of x and y in the resultant matrix are:')
for i in final:
    print(i[0],i[1])
        
    
    
        

    