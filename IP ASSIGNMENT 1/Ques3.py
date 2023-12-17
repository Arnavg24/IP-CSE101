x0=float(input("Initial x co-ordinate:"))
y0=float(input("Initial y co-ordinate:"))
x=x0
y=y0
var=0
dist=float(input("please enter the distance:"))
while dist>0:
     if dist<=25:
         y=y+dist
     elif dist>25 and dist<=50:
         y=y-dist
     elif dist>50 and dist<76:
         x=x+dist
     elif dist>=76:
         x=x-dist
     var=var+dist
     dist=float(input("please enter the distance:"))
print("Final Co-ordinates:(",x,",",y,")",sep="")
print("total distance travelled:",var)
print("distance formula:",((x0-x)**2+(y0-y)**2)**0.5)

    