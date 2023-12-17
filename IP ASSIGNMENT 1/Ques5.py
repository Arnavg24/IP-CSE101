def fact(x): 
  if x>0: 
    x = x*fact(x-1) 
  if x==0: 
    return 1 
  return x 

def sin(a):
  a=a*3.14/180
  return a-a**3/fact(3)+a**5/fact(5)-a**7/fact(7)+a**9/fact(9)-a**11/fact(11)+a**13/fact(13)-a**15/fact(15)+a**17/fact(17)-a**19/fact(19)

def cos(x):
  x=x*3.14/180
  return 1-x**2/fact(2)+x**4/fact(4)-x**6/fact(6)+x**8/fact(8)-x**10/fact(10)+x**12/fact(12)-x**14/fact(14)+x**16/fact(16)-x**18/fact(18)

def tan(x):
  return sin(x)/cos(x)

angle=float(input('Please enter the angle (in degrees):'))
dist=int(input('Please enter the distance:'))
print('height of the pole=',round(tan(angle)*dist,2))
print('distance to the tip of the pole=',round(dist/cos(angle),2))