def profit(m,x1,x2):
    z=0
    if(x1<m and x2<m):
        z=x1*90+x2*30
    elif(x1>m and x2>m):
        z=90*m+(x1-m)*100+25*m+30*(x2-m)
    elif(x1<m and x2>m):
        z=90*x1+25*m+30*(x2-m)
    else:
        z=90*m+(x1-m)*100+25*x2
    return z
        
def constraint(x1,x2):
    return 4*x1+x2<=200 and 2*x1+x2<=120

x1=list(range(60))
x2=list(range(120))
x1_p,x2_p=-1, -1
max_p=-1
m=int(input("Enter value of M:"))
for i in x1:
    for j in x2:
        if(constraint(i,j)):
            Z=profit(m,i,j)            
            if(Z>max_p):
                max_p=Z
                x1_p=i
                x2_p=j            
print("Number of chairs=",x1_p,sep="")
print("Number of tables=",x2_p,sep="")
print("profit=",max_p,sep="")
