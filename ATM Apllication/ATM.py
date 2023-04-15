from cardholder import *


def print_language():
    print('Choose one of these languages😊')
    print('1.Azərbaycan dili')
    print('2.Русский')
    print('3.English')
def print_data_az():
    print('Bunlardan birini seçin')
    print('1.Depozit')
    print('2.Pul çəkmək')
    print('3.Balans')
def print_data_rus():
    print('Выберите одну из операций')
    print('1.Депозит')
    print('2.Снять деньги')
    print('3.Баланс')
    
def print_data_eng():
    print('Choose one of this options')
    print('1.Deposit')
    print('2.Withdraw money')
    print('3.Balance')
def deposit_az(cardholder):
    try:
        deposit = float(input('Neçə AZN yatırmaq istəyirsiniz?'))
        cardholder.set_balance(cardholder.get_balance()+deposit)
        print('Təşəkkür edirik.Sizin yeni məbləğiniz {} AZN'.format(str(cardholder.get_balance())))
    except:
        print('Məlumat yanlışdı')
def deposit_rus(cardholder):
    try:
        deposit = float(input('Сколько AZN хотите вложить?'))
        cardholder.set_balance(cardholder.get_balance()+deposit)
        print('Спасибо. Ваш новый баланс {} AZN'.format(str(cardholder.get_balance())))
    except:
        print('Неверная информация')

def deposit_eng(cardholder):
    try:
       deposit = float(print('How much AZN do you want to invest?'))
       cardholder.set_balance(cardholder.get_balance()+deposit)
       print('Thank you. Your new balance is {} AZN'.format(str(cardholder.get_balance())))
    except:
        print('Invalid information')
def withdraw_az(cardholder):
    try:
        withdraw = float(input('Neçə manat çəkmək istəyirsiniz?'))
        if (cardholder.get_balance())<withdraw:
            print('Balansda kifayət qədər məbləğ yoxdur')
        else:
            cardholder.set_balance(cardholder.get_balance()-withdraw)
            print('Təşəkkür edirik')
    except:
        print('Yanlış məlumat')
def withdraw_rus(cardholder):
    try:
        withdraw = float(input('Сколько манатов хотите снять?'))
        if cardholder.get_balance()<withdraw:
            print('Нет достаточно манатов')
        else:
            cardholder.set_balance(cardholder.get_balance()-withdraw)
            print('Спасибо!')
    except:
        print('Неверная информация')

def withdraw_eng(cardholder):
    try:
        withdraw = float(input('How many manats do you want to withdraw?'))
        if cardholder.get_balance()<withdraw:
            print('Insufficient balance')
        else:
            cardholder.set_balance(cardholder.get_balance()-withdraw)
            print('Thank you!')
    except:
        print('Invalid information')

def check_balance_az(cardholder):
    currentUser = cardholder('','','','','')
    list_of_cardholders = []
    list_of_cardholders.append(cardholder('440923455342',1256,'Namiq','Planov',256.68))
    list_of_cardholders.append(cardholder('345612732890',5790,'Əli','Məmmədov',156.68))
    list_of_cardholders.append(cardholder('145876903241',1352,'Vəli','Əliyev',136))
    list_of_cardholders.append(cardholder('798657093216',7094,'Mahmud','Xasayev',498))
    list_of_cardholders.append(cardholder('987060543271',1913,'Xalid','Basayev',76.43))
    list_of_cardholders.append(cardholder('556789356210',5234,'Polad','Qəniyev',15.79))

    debitcard = ''
    while True:
        try:
            debitcard = int(input('Kartı daxil edin'))
            debitmacth = [holder for holder in list_of_cardholders if holder.cardNumber ==debitcard]
            if len(debitmacth)>0:
                current_user = debitmacth[0]
                break
            else:
                print('Kartın nömrəsi səhvdi')
        except:
             print('Kartın nömrəsi səhvdi')
        
    while True:
        try:
            userpin = int(input('Şifrəni daxil edin:').strip())
            if current_user.get_pin()==userpin:
                break
            else:
                print('Şifrə yanlışdı.Təkrar edin')
        except:
            print('Şifrə yanlışdı.Təkrar edin')
    print('Xoş gəlmisiniz, ',current_user.get_firstname())
    option = 0
    while option!=4:
        print_data_az()
        try:
            option = int(input())
        except:
            print('Yanlış məlumat')
        if option ==1:
            deposit_az(current_user)
        elif option==2:
            withdraw_az(current_user)
        elif option==3:
            check_balance_az(current_user)
        else:
            option =0
    print('Təşəkkür edirik')





def check_balance_rus(cardholder):
    currentUser = cardholder('','','','','')
    list_of_cardholders = []
    list_of_cardholders.append(cardholder('440923455342',1256,'Namiq','Planov',256.68))
    list_of_cardholders.append(cardholder('345612732890',5790,'Əli','Məmmədov',156.68))
    list_of_cardholders.append(cardholder('145876903241',1352,'Vəli','Əliyev',136))
    list_of_cardholders.append(cardholder('798657093216',7094,'Mahmud','Xasayev',498))
    list_of_cardholders.append(cardholder('987060543271',1913,'Xalid','Basayev',76.43))
    list_of_cardholders.append(cardholder('556789356210',5234,'Polad','Qəniyev',15.79))

    debitcard = ''
    while True:
        try:
            debitcard = int(input('Вставьте карту'))
            debitmacth = [holder for holder in list_of_cardholders if holder.cardNumber ==debitcard]
            if len(debitmacth)>0:
                current_user = debitmacth[0]
                break
            else:
                print('Номер карты неверный')
        except:
             print('Номер карты неверный')


def check_balance_eng(cardholder):
    currentUser = cardholder('','','','','')
    list_of_cardholders = []
    list_of_cardholders.append(cardholder('440923455342',1256,'Namiq','Planov',256.68))
    list_of_cardholders.append(cardholder('345612732890',5790,'Əli','Məmmədov',156.68))
    list_of_cardholders.append(cardholder('145876903241',1352,'Vəli','Əliyev',136))
    list_of_cardholders.append(cardholder('798657093216',7094,'Mahmud','Xasayev',498))
    list_of_cardholders.append(cardholder('987060543271',1913,'Xalid','Basayev',76.43))
    list_of_cardholders.append(cardholder('556789356210',5234,'Polad','Qəniyev',15.79))

    debitcard = ''
    while True:
        try:
            debitcard = int(input('Insert your card'))
            debitmacth = [holder for holder in list_of_cardholders if holder.cardNumber ==debitcard]
            if len(debitmacth)>0:
                current_user = debitmacth[0]
                break
            else:
                print('Invalid card number')
        except:
             print('Invalid card number')
    





    
    


