import mysql.connector
from datetime import timedelta,datetime


conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='namiq2003123.',
    database='ticket_info',
    port = '3307'
)

cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings_db (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    passport VARCHAR(255),
    citizenship VARCHAR(255),
    plane VARCHAR(255),
    country VARCHAR(255),
    airport VARCHAR(255),  
    luggages INT,
    seat_num INT,
    payment INT,
    timestamp TIMESTAMP
)

''')



class Booking:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = ""
        self.passport = ""
        self.citizenship=""
        self.plane = ""
        self.country = ""
        self.airport = ""
        self.luggages = ""
        self.seat_num = ""
        self.payment = ""


    def info(self):
        
        starting = 'Welcome to our ticket order company😊'
        print(starting)
        dash1 = '--------------------------------------'
        print(dash1)
        prices = 'Our prices depend on the type of the seat of the airplane'
        print(prices)
        dash2 = '---------------------------------------------------------'
        print(dash2)
        seats = input('Which of seats are you interested in?')
        print(seats)
        if seats == 'econom class' or seats=='econom':
            print('the price of the seat of the econom class is 70 AZN')
        elif seats =='standart class' or seats =='standart':
             print('the price of the seat of the standart class is 150 AZN')
        elif seats =='vip' or seats=='vip class':
             print('the price of the seat of the VIP class is 270 AZN')
        else:
            input('not valid class of seats.Enter valid class:')
    def buying_ticket(self,seats,payment):
        number_of_seats = 200
        timestamp = datetime.now()
        
        while True:
            self.first_name = input('enter first name:')
            self.last_name = input('enter last name:')
            age = int(input('enter age please:'))
            if age<14:
                input('there will be a discount of 25% '+'for the guest who is younger than 14😊-')
            passport = str(input('enter you passport sery:'))
            citizenship = input('enter the country of which guest is citizen:')
            plane = input('In which airplane do you want to go?')
            country = input('To whcih country do you want to go?')
            airport = input('From which airport do you want to go?')
            
            luggages = int(input('how many additional luggages will you take with you into the plane? One luggage is 80 AZN.-'))
            seat_num = int(input('enter the seat number please:'))
            if age<14:
                if seats == 'econom':
                    payment = (70-(70/4))+(luggages*80)
                    print('Payment will be {} AZN'.format(payment))
                elif seats == 'standart':
                    payment = (150-(150/4))+(luggages*80)
                    print('Payment will be {} AZN'.format(payment))
                elif seats == 'vip':
                    payment = (270-(270/4))+(luggages*80)
                    print('Payment will be {} AZN'.format(payment)) 
            else:
                if seats == 'econom':
                    payment = (70)+(luggages*80)
                    print('Payment will be {} AZN'.format(payment))
                elif seats == 'standart':
                    payment = (150)+(luggages*80)
                    print('Payment will be {} AZN'.format(payment))
                elif seats == 'vip':
                    payment = (270)+(luggages*80)
                    print('Payment will be {} AZN'.format(payment))
            seats = [True] * number_of_seats
            if seat_num<1 or seat_num >number_of_seats:
                seat_num = int(input('Invalid seat number.Please enter valid seat number:'))
                
                
            elif seats[seat_num-1]:
                cursor.execute("INSERT INTO bookings_db (first_name, last_name, age, passport, citizenship, plane, country, airport,luggages, seat_num, payment) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
               (self.first_name, self.last_name, age, passport, citizenship, plane, country, airport,luggages,seat_num, payment))
                conn.commit()
                buying = print('This seat is available.Your bought this seat.Thank you {}😊'.format(self.first_name))
                break
                
            else:
                taken_seat = int(input('Seat {} is taken unfortuntely😥.Please enter the free seat:'))
                print('thank you')

                
                

                    
        








