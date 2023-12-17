n=int(input("Please enter the value of n:"))
for i in range(1,n+1):
    for j in range(0,i):
        print('*',end='')
    for j in range(1,2*(n-i)+1):
        print(' ',end='')
    for j in range(0,i):
        print('*',end='')
    print()