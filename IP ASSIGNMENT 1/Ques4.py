a=float(input("Starting time:"))
b=float(input("Ending time:"))
distance=0
t=a
import math
while t<b: 
    v=2000*(math.log(140000/(140000-2100*t)))-9.8*t
    v_1=2000*(math.log(140000/(140000-2100*(t+0.25))))-9.8*(t+0.25)
    v_av=(v+v_1)/2  
    distance +=v_av*0.25
    t+=0.25
print(distance)
