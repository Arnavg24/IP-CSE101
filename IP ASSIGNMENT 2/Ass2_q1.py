menu = [("Samosa  ", 15), ("Idli     ", 30), ("Maggie  ", 50), ("Dosa    ", 70), ("Tea     ", 10), ("Coffee  ", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print('\tMenu')
opt=1
for i in menu:
    print(str(opt)+')',i[0]+'\t',i[1],sep='')
    opt+=1
print()
l=[]
inp_list = list(map(int,input('Enter item number followed by quantity:').split()))
while inp_list!=[]:   
    l.append((inp_list[0],inp_list[1]))
    inp_list = list(map(int,input('Enter item number followed by quantity:').split()))
    
for i in l:
    if i[0]>len(menu) or (i[0]<0):
        print('item number',i[0],'not in list')
        l.remove(i)
        
ans=[]
for i in l:
    y=menu[i[0]-1]
    price=i[1]*y[1]
    ans.append((y[0],i[1],price)) 
print()
print('\tBill')
for i in ans:
    print(i[0].strip()+',',str(i[1])+', Rs.'+str(i[2]))
print('Total',sum([i[1] for i in ans]),'items, Rs',sum([i[2] for i in ans]))   