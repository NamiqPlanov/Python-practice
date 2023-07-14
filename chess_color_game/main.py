from chesscolor_guess import *

ui = UserInterface()

while True:
    language = input('enter language:')
    if language =='english':
        print(ui.game_eng())
    elif language =='azeri':
        ui.game_az()
    elif language =='russian':
        ui.game_ru()
    else:
        print('not real language')