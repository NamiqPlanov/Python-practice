from cardholder import cardholder
def print_data_az():
    print('Bunlardan birini seçin')
    print('1.Depozit')
    print('2.Pul çəkmək')
    print('3.Balans')

def deposit_az(cardholder):
    try:
        deposit = float(input('Neçə AZN yatırmaq istəyirsiniz?'))
        cardholder.set_balance(cardholder.get_balance()+deposit)
        print('Təşəkkür edirik.Sizin yeni məbləğiniz {} AZN'.format(str(cardholder.get_balance())))
    except:
        print('Məlumat yanlışdı')

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





    





    
    


