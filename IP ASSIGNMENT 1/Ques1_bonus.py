x=int(input("Enter the number:"))
x1=x//10000000

y=x1//10
z=x1%10
if y==0:
    a=""
elif y==2:
    a="twenty"
elif y==3:
    a="thirty"
elif y==4:
    a="forty"
elif y==5:
    a="fifty"
elif y==6:
    a="sixty"
elif y==7:
    a="seventy"
elif y==8:
    a="eighty"
elif y==9:
    a="ninety"
if x1==10:
    a="ten"
elif x1==11:
    a="eleven"
elif x1==12:
    a="twelve"
elif x1==13:
    a="thirteen"
elif x1==14:
    a="fourteen"
elif x1==15:
    a="fifteen"
elif x1==16:
    a="sixteen"
elif x1==17:
    a="seventeen"
elif x1==18:
    a="eighteen"
elif x1==19:
    a="nineteen"
if z==0:
    b=""
elif z==1:
    b="one"
elif z==2:
    b="two"
elif z==3:
    b="three"
elif z==4:
    b="four"
elif z==5:
    b="five"
elif z==6:
    b="six"
elif z==7:
    b="seven"
elif z==8:
    b="eight"
elif z==9:
    b="nine"
if x1!=0:
    if z==0 or y==1:
        print(a, "crore ", end='')
    else:
        print(a,b,"crore ", end='')
x=x%10000000

x1=x//100000
y=x1//10
z=x1%10
if y==0:
    a=""
elif y==2:
    a="twenty"
elif y==3:
    a="thirty"
elif y==4:
    a="forty"
elif y==5:
    a="fifty"
elif y==6:
    a="sixty"
elif y==7:
    a="seventy"
elif y==8:
    a="eighty"
elif y==9:
    a="ninety"
if x1==10:
    a="ten"
elif x1==11:
    a="eleven"
elif x1==12:
    a="twelve"
elif x1==13:
    a="thirteen"
elif x1==14:
    a="fourteen"
elif x1==15:
    a="fifteen"
elif x1==16:
    a="sixteen"
elif x1==17:
    a="seventeen"
elif x1==18:
    a="eighteen"
elif x1==19:
    a="nineteen"
if z==0:
    b=""
elif z==1:
    b="one"
elif z==2:
    b="two"
elif z==3:
    b="three"
elif z==4:
    b="four"
elif z==5:
    b="five"
elif z==6:
    b="six"
elif z==7:
    b="seven"
elif z==8:
    b="eight"
elif z==9:
    b="nine"
if x1!=0:
    if z==0 or y==1:
        print(a, "lakhs ", end='')
    else:
        print(a,b,"lakhs ", end='')
x=x%100000

x1=x//1000
y=x1//10
z=x1%10
if y==0:
    a=""
elif y==2:
    a="twenty"
elif y==3:
    a="thirty"
elif y==4:
    a="forty"
elif y==5:
    a="fifty"
elif y==6:
    a="sixty"
elif y==7:
    a="seventy"
elif y==8:
    a="eighty"
elif y==9:
    a="ninety"
if x1==10:
    a="ten"
elif x1==11:
    a="eleven"
elif x1==12:
    a="twelve"
elif x1==13:
    a="thirteen"
elif x1==14:
    a="fourteen"
elif x1==15:
    a="fifteen"
elif x1==16:
    a="sixteen"
elif x1==17:
    a="seventeen"
elif x1==18:
    a="eighteen"
elif x1==19:
    a="nineteen"
if z==0:
    b=""
elif z==1:
    b="one"
elif z==2:
    b="two"
elif z==3:
    b="three"
elif z==4:
    b="four"
elif z==5:
    b="five"
elif z==6:
    b="six"
elif z==7:
    b="seven"
elif z==8:
    b="eight"
elif z==9:
    b="nine"
if x1!=0:
    if z==0 or y==1:
        print(a, "thousand ", end='')
    else:
        print(a,b,"thousand ", end='')
x=x%1000
z=x//100
if z==0:
    b=""
elif z==1:
    b="one"
elif z==2:
    b="two"
elif z==3:
    b="three"
elif z==4:
    b="four"
elif z==5:
    b="five"
elif z==6:
    b="six"
elif z==7:
    b="seven"
elif z==8:
    b="eight"
elif z==9:
    b="nine"
if z==0:
    print("", end='')
else:
    print(b,"hundred ", end='')
x=x%100
y=x//10
z=x%10
if y==0:
    a=""
elif y==2:
    a="twenty"
elif y==3:
    a="thirty"
elif y==4:
    a="forty"
elif y==5:
    a="fifty"
elif y==6:
    a="sixty"
elif y==7:
    a="seventy"
elif y==8:
    a="eighty"
elif y==9:
    a="ninety"
if z==0:
    b=""
elif z==1:
    b="one"
elif z==2:
    b="two"
elif z==3:
    b="three"
elif z==4:
    b="four"
elif z==5:
    b="five"
elif z==6:
    b="six"
elif z==7:
    b="seven"
elif z==8:
    b="eight"
elif z==9:
    b="nine"
if x==10:
    a="ten"
elif x==11:
    a="eleven"
elif x==12:
    a="twelve"
elif x==13:
    a="thirteen"
elif x==14:
    a="fourteen"
elif x==15:
    a="fifteen"
elif x==16:
    a="sixteen"
elif x==17:
    a="seventeen"
elif x==18:
    a="eighteen"
elif x==19:
    a="nineteen"
if z==0 or y==1:
    print(a)
else:
    print(a,b)
