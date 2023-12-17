wts = [(10,5),(20,5),(100,15),(50,10),(50,10),(50,10),(100,45)]
f = open("./q6.txt", "r")
inputs=f.read().split("\n")

w=open("./IPgrades.txt", "w+")


for student in inputs:
    l1=list(map(int,student.split(",")))
    marks=l1[1:]
    roll_no=l1[0]
    totmarks=0
    for i in range(len(marks)):
        weighted_marks=(float(marks[i])/wts[i][0])*wts[i][1]
        totmarks+=weighted_marks
    grade=''
    if(totmarks>80):
        grade='A'
    elif(70<totmarks<=80):
        grade='A-'
    elif(60<totmarks<=70):
        grade='B'
    elif(50<totmarks<=60):
        grade='B-'
    elif(40<totmarks<=50):
        grade='C'
    elif(35<totmarks<=40):
        grade='C-'
    elif(30<totmarks<=35):
        grade='D'
    else:
        grade='F'
    w.write(f"{roll_no},{round(totmarks,2)}, {grade}\n")