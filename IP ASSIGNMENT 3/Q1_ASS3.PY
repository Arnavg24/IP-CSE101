n=int(input('enter value of n:'))

def upp(x):
    if x==0:
        return ''
    else:
        return '* '*x +'  '*(n-x)*2+ '* '*x+ '\n'+ upp(x-1)
    
def loww(x):
    if x==1:
        return ''
    else:
        return '* '*(n-x+2) + 2*'  '*(x-2) + '* '*(n-x+2) +'\n'+ loww(x-1)
    
print(upp(n)+loww(n))   