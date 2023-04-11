from journal import *

namiq = Student('Namiq','Planov','Saleh')
eli = Student('Eli','Abdullayev','Konul')
qumru = Student('Qumru','Eliyeva')
qumru.makeStarosta()

group_2450i = Group('2450i', qumru)
subject_oop = Subject('Object Oriented Programming','OOP')
mammad = Teacher('Mammad','Shahmaliyev','Oqtay',subject_oop)

group_2450i.addStudent(namiq)
group_2450i.addStudent(eli)

group_2450i.addSubject(subject_oop)
group_2450i.printStudentList()
group_2450i.printSubject()
