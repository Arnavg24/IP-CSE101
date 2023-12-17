w_pop = [50, 1450, 1400, 1700,  1500, 600, 1200]
inc=2.5
inc_new=inc

a = 0
for i in range(7):
    w_pop[i]=w_pop[i]
total_pop=0
for i in w_pop:
    total_pop = total_pop + i 
print("current total population is : ",total_pop)
j=0
current_pop=total_pop
previous_pop=0
while (current_pop>=previous_pop):
    previous_pop=total_pop
    for i in range(7):
        w_pop[i]=w_pop[i]+(w_pop[i]*inc)/100
        inc-=0.4
    total_pop=0
    for i in w_pop:
        total_pop+=i
    current_pop=total_pop
    inc_new-=0.1
    inc=inc_new
    j+=1
print("population is at maximum at ",j-1," years with total population",previous_pop)