cost=float(input('Enter cost:'))
allowance=float(input('Enter allowance:'))
sf=float(input('Enter saving fraction:'))
r=float(input('Enter rate of interest:'))
savings,month = 0,0
while cost > savings:
    month_saving=sf*allowance
    month=month+1
    savings=month_saving+savings*(1 +r/100)
    rem_savings =savings-cost
    
   
print(month,round(rem_savings,2)) 
  
  
    
    