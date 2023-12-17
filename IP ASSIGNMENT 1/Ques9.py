def d(p):
    e=2.71828182845
    a=10
    b=1.05    
    return e**(a-b*p)

def s(p):
    e=2.71828182845
    c=1
    d=1.06
    return e**(c+d*p)
mp=1.0
ans=-1
while mp<=200:
    
    if(abs(d(mp)-s(mp))<=30):
        ans=mp
        
        break
    mp*=1.05
        
    
if(ans==-1):
    print("No Equilibrium Solution")
else:
    print("Equilibrium Price: ",ans)
    print("Demand: ",d(ans))
    print("Supply: ",s(ans))

