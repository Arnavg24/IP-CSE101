cname,credits=map(str,input('Please enter course name and credits resp. :').split())
credits=int(credits)

assessments=[]
while True:
    x,y=input("Enter assessment type and it's weight resp. :").split()
    y=int(y)
    assessments.append((x,y))
    if sum([i[1] for i in assessments]) ==100:
        break
    elif sum([i[1] for i in assessments]) > 100:
        print('weight sum exceeded 100,please fill the assessments again')
        assessments.clear()

max_marks=list(map(int,input('enter max marks possible in assessments resp.').split()))
policy=[80,65,50,40]

course = (cname, credits, assessments, policy)
print(cname,'course created with details',course)


f = open("marks.txt", "r")
inputs=f.read().split("\n")
# print(inputs)

# final_marks=[]#list containing final marks of students
dic={} #roll no key marks value
for student in inputs:
    l1=list(map(int,student.split()))
    marks=l1[1:]
    roll_no=l1[0]
    tot_marks=0
    for i in range(len(marks)):
        weight_marks=(float(marks[i])/max_marks[i])*assessments[i][1] 
        tot_marks+=weight_marks
    # final_marks.append(tot_marks)
    dic[roll_no]=tot_marks
# print(dic)

# the below function find the 2 consecutive elements with max diff and returns their average
def avg_max_diff(x):
    x.sort()
    # print(x)
    max_diff = 0
    answer=[]
    for i in range(len(x) - 1):
        diff = x[i + 1] - x[i]
        if abs(diff) > abs(max_diff):
            max_diff = diff
            answer = (x[i] + x[i + 1])/2
            # print(answer)
    return answer
        
           
a=[]
b=[]
c=[]
d=[]
for h,i in dic.items():
    if 78<=i<=82:
        a.append(i)
    elif 63<=i<=67:
        b.append(i)
    elif 48<=i<=52:
        c.append(i)
    elif 38<=i<=42:
        d.append(i)
        
a_f=avg_max_diff(a)
b_f=avg_max_diff(b)
c_f=avg_max_diff(c)
d_f=avg_max_diff(d)

if a_f!=[]:
    policy[0]=avg_max_diff(a)
else:
    policy[0]=80

if b_f!=[]:
    policy[1]=avg_max_diff(b)
else:
    policy[1]=65

if c_f!=[]:
    policy[2]=avg_max_diff(c)
else:
    policy[2]=50

if d_f!=[]:
    policy[3]=avg_max_diff(d)
else:
    policy[3]=40

for h,i in dic.items():
    if i>policy[0]:
        dic[h]=i,'A'


    if i>policy[1] and i<policy[0]:
        dic[h]=i,'B'
 
    if i>policy[2]  and i<policy[1] :
        dic[h]=i,'C'

   
    if i>policy[3]  and i<policy[2] :
        dic[h]=i,'D'

               
    if i<policy[3]:
       dic[h]=i,'F'


   
grade_cutoffs={'A':policy[0], 'B':policy[1], 'C':policy[2], 'D':policy[3], 'F':'Less than '+str(policy[3])}
print(dic)
print(grade_cutoffs)


# grade summary
def counter(grade):
    count=0
    for value in dic.values():
        if value[1]==grade:
            count+=1
    return count

grade_summary={'A':counter('A'),'B':counter('B'),'C':counter('C'),'D':counter('D'),'F':counter('F'),}
        
print(grade_summary)







while True:
    print('1)Generate Summary')
    print('2)Print the grade of all students')
    print('3)Search for a student record')
    print('4)Exit')
    
    
    choice=int(input())
    
    if choice==4:
       break
   
    elif choice==1:
        print('course info',course)
        print('cutoffs for diff grades:',grade_cutoffs)
        print('grade summary',grade_summary)
        
    elif choice==2:
        with open ('Q5_out.txt','w') as file:
            for roll in dic:
                line=str(roll)+': Total Marks = '+str(dic[roll][0])+', Grade = '+str(dic[roll][1])+'\n'
                file.write(line)
            
    elif choice==3:
        roll=int(input('Enter the roll number:'))
        if roll in dic:
            print(str(roll)+': Total Marks = '+str(dic[roll][0])+', Grade = '+str(dic[roll][1]))
        else:
            print('Roll number not found')