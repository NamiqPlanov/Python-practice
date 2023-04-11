from journal import *

n = int(input('Enter the number of students(first student must be starosta):'))
students_arr=[]
for i in range(1,n+1):
    student_input = input('Enter student #{}:name,last_name,father_name: '.format(i)).split(' ')
    first_name = student_input[0].strip()
    last_name = student_input[1].strip() if len(student_input)>1 else None
    father_name = student_input[2].strip() if len(student_input) >2 else None

    student = Student(first_name,last_name,father_name)
    if i==1:
        student.makeStarosta()
    students_arr.append(student)


group_name = input('enter group name:')
group = Group(group_name,students_arr[0])
print('group created:',group)

subject = input('Enter subject name:')
subject = Subject(subject.split(',')[0].strip(),subject.split(',')[1].strip())
print('Subject created:',subject)
group.addSubject(subject)

teacher_input = input('Enter teachername,lastname,fahtername:').split(' ')
first_name = teacher_input[0].strip()
last_name = teacher_input[1].strip() if len(teacher_input)>1 else None
father_name = teacher_input[2].strip() if len(teacher_input)>2 else None
teacher = Teacher(first_name,last_name,father_name,subject)

for i in range(1,len(students_arr)):
    group.addStudent(students_arr[i])

group.printStudentList()
group.printSubject()