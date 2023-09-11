class Booking:
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
        if seats == 'econom class':
            print('the price of the seat of the econom class is 70 AZN')
        elif seats =='standart class':
             print('the price of the seat of the standart class is 150 AZN')
        else:
             print('the price of the seat of the VIP class is 270 AZN')
    def buying_ticket(self):
        g = 0
        number_of_seats = 200
        num = int(input('Enter number of tickets that you want to buy:'))
        while g<num:
            first_name = input('enter first name:')
            last_name = input('enter last name:')
            age = int(input('enter age please:'))
            if age<14:
                input('there will be a discount of 25% '+'for the guest who is younger than 14😊-')
            passport = str(input('enter you passport sery:'))
            citizenship = input('enter the country of which guest is citizen:')
            seat_num = int(input('enter the seat number please:'))
            seats = [True] * number_of_seats
            if seat_num<1 or seat_num >number_of_seats:
                seat_num = int(input('Invalid seat number.Please enter valid seat number:'))
            elif seats[seat_num-1]:
                buying = input('This seat is available.Your bought this seat.Thank you {}😊'.format(first_name))
            else:
                taken_seat = int(input('Seat {} is taken unfortuntely😥.Please enter the free seat:'))
                print('thank you')
                

                    
        








