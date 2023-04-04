from student import *
from group import *
from subject import *



Namiq = Student('Namiq','Planov','Saleh')
print(Namiq.GetfullName())

Ali = Student('Ali','Abdullayev','Konul')
print(Ali.GetfullName())
Eltun = Student('Eltun','Xelilov')
Eltun.father_name = 'Nemet'
print('Eltun is starosta',Eltun.isstarosta())
Namiq.makestarosta()

group = Group('2450i', Namiq)
print('group:',group)

Mammad = Teacher('Mammad', 'Shahmaliyev')
print('teacher:',Mammad)

subject = Subject('Object Oriented Programming', 'OOP')
print('subject:',subject)
