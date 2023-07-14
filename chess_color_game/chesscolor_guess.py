

class UserInterface:

    def game_eng(self):
        name = input('enter name please: ')
        lastname = input('enter lastname please: ')
        age = int(input('enter age please: '))
        s = input('enter the coordinate:')
        if s[0] =='a' or s[0]=='c' or s[0]=='e' or s[0]=='g':
            if int(s[1])%2==0:
                print('white')
            else:
                print('black')
        else:
            if int(s[1])%2==0:
                print('black')
            else:
                print('white')

    def game_az(self):
        name = input('Adınızı daxil edin: ')
        lastname = input("Soyadınızı daxil edin: ")
        age = int(input("Yaşınızı daxil edin: "))
        a = input('Koordinatı daxil edin:')
        if a[0] =='a' or a[0]=='c' or a[0]=='e' or a[0]=='g':
            if int(a[1])%2==0:
                print('Ağ')
            else:
                print('Qara')
        else:
            if int(a[1])%2==0:
                print( 'Qara')
            else:
                print('Ağ')
    def game_ru(self):
        name = input('Ваше имя: ')
        lastname = input('Ваша фамилия: ')
        age = int(input('Сколько вам лет: '))
        r = input('введите координат: ')
        if r[0]=='a' or r[0] =='c' or r[0] =='e' or r[0] =='g':
            if int(r[1])%2==0:
                print('Белый')
            else:
                print('Черный')
        else:
            if int(r[1])%2==0:
                print('Черный')
            else:
                print('Белый')
                



