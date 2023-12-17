
class Course:
    def __init__(self):
        self.cname = cname
        self.credits = credits
        self.assessment = assessments
        self.policy = policy

class Student:
    def __init__(self, roll_nos, marks):
        self.number = len(roll_nos)
        self.roll_nos = roll_nos
        self.marks = marks
        
        
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
# assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)]
policy = [80, 65, 50, 40]
course = (cname, credits, assessments, policy)


class Grading:
    def __init__(self, cname, credits, assessments, policy):
        self.cname = cname
        self.credits = credits
        self.assessments = assessments
        self.policy = policy
        self.students = {}
        
    def upload_marks(self, file):
        with open(file) as f:
            for line in f:
                rollno, *marks = map(float, line.strip().split())
                total = sum(marks)
                grade = 'F'
                for i in range(len(self.policy) - 1):
                    if total >= self.policy[i]:
                        grade = 'ABCD'[i]
                        break
                    
                self.students[rollno] = (total, grade)
                
    def do_grading(self):
        pass
    
    def generate_summary(self):
        print("Course Info:")
        print("Name:", self.cname)
        print("Credits:", self.credits)
        print("Assessments:", self.assessments)
        print("Policy:", self.policy)
        print("Grading Summary:")
        grades = [0] * 6
        for _, (total, grade) in self.students.items():
            grades[ord(grade) - ord('A')] += 1
        for i in range(6):
            print(f"{'ABCDF'[i]}:{grades[i]}")
            
    def print_grades(self, file):
        with open(file, 'w') as f:
            for rollno, (total, grade) in self.students.items():
                f.write(f"{rollno},{total},{grade}\n")
                
    def search_student(self, rollno):
        if rollno in self.students:
            total, grade = self.students[rollno]
            print(f"Roll No: {rollno}\nTotal: {total}\nGrade: {grade}")
        else:
            print(f"Student with roll no {rollno} not found.")





ip = Grading(cname, credits, assessments, policy)
ip.upload_marks('marks.txt')
ip.do_grading()

while True:
    choice = input("Enter 1 to generate summary, 2 to print grades, 3 to search for student, or press enter to exit: ")
    if choice == '1':
        ip.generate_summary()
    elif choice == '2':
        ip.print_grades('grades.txt')
    elif choice == '3':
        rollno = int(input("Enter roll no: "))
        ip.search_student(rollno)
    else:
        break
