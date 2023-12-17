l=[]
inp_list = list(map(str,input('Enter  course_no, number_of_credits and grade_received respectively:').split()))
while inp_list!=[]:
    course_code=''
    valid_1=inp_list[0].isalnum()
    digit=False
    for i in inp_list[0]:
        if i.isalpha() and digit:
            valid_1=False
            break
        elif i.isupper():
            course_code+=i
        elif i.isdigit() and course_code!='':
            digit=True   
        else:
            valid_1=False
            print('Incorrect course number')
            break
    if inp_list[1] in ('1','2','4'):
        valid_2=True
    else:
        valid_2=False
        print('Incorrect grade credits')
    if inp_list[2] in ('A+','A','A-','B','B-','C','C-','D','F'):
        valid_3=True      
    else:
        valid_3=False
        print('Incorrect grade')
    valid=valid_1 and valid_2 and valid_3
    if valid==True:
      l.append((inp_list[0],inp_list[1],inp_list[2]))
    inp_list = list(map(str,input('Enter  course_no, number_of_credits and grade_received respectively:').split()))
    
    
l_sort = sorted(l,key=lambda i:i[0]) #lambda x:x[0] is to extract the course number as a key to sort the list with.
for i in l_sort:        
    print(i[0],':',i[2],sep='')
    
grade_lst=[]
for i in l_sort:   
    if i[2] =='A+':
        grade = 10
    elif i[2] =='A':
        grade = 10
    elif i[2] =='A-':
        grade = 9
    elif i[2] =='B':
        grade = 8
    elif i[2] =='B-':
        grade = 7
    elif i[2] =='C':
        grade = 6
    elif i[2] =='C-':
        grade = 5
    elif i[2] =='D':
        grade = 4
    elif i[2] =='F':
        grade = 2
    grade_lst.append(grade)

a,b=0,0    
for i in range(len(l_sort)):
    a+=(int(l_sort[i][1])*grade_lst[i])
    b+=int(l_sort[i][1])
sgpa=round(a/b,2)
print('SGPA:',sgpa)