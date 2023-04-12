gender = input('Enter your gender: ')
name = input('Enter your name {}:'.format(gender))
start = input('For starting type start: ')



if start.lower() =='start':
    print("Let's start {}".format(name))
else:
    quit()

points = 0

question = input('When was First World War occured?')
if question == 1914:
    print('Correct! 😉')
    points+=50
else:
    print('Incorrect answer 🤨')

question = input('When was the Contract of Century signed?')
if question ==1944:
    print('Correct! 😉')
    points+=60
else:
    print('Incorrect answer 🤨')
    points-=50

question = input('Who is the president of Russia?')
if question.lower() =='Putin ':
    print('Correct! 😉')
    points+=150
else:
    print('Incorrect answer 🤨')
    points-=70

question = input('Which club was the champion in MPL in 2021?')
if question.upper() =='Neftchi':
    print('Correct! 😉')
    points+=250
else:
    print('Incorrect answer 🤨')
    points-=150

question = input('What type of programming language is Python?')
if question.upper() =='OOP':
    print('Correct! 😉')
    points+=100
else:
    print('Incorrect answer 🤨')
    points-=50

question = input('For how many year is Formula 1 being held in Baku?')
if question ==6:
    print('Correct! 😉')
    points+=200
else:
    print('Incorrect answer 🤨')
    points-=90

if points>=100:
   print('You have scored {} points!😎'.format(points))
else:
    print('You have scored {} points.😕'.format(points))

