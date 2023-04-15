class cardholder:
    def __init__(self,cardNumber:int,pin:int,first_name:str,last_name:str,balance:float):
        self.cardNumber = cardNumber
        self.pin = pin
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance

    def get_cardnumber(self):
        return self.cardNumber
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.first_name
    def get_lastname(self):
        return self.last_name
    def get_balance(self):
        return self.balance
    def set_cardnumber(self,newval):
        self.cardNumber = newval
    def set_pin(self,newval):
        self.pin = newval
    def set_firstname(self,newval):
        self.first_name = newval
    def set_lastname(self,newval):
        self.last_name = newval
    def set_balance(self,newval):
        self.balance = newval

    def get_info(self):
        print('Card number: {}'.format(self.cardNumber))
        print('Pin: {}'.format(self.pin))
        print('Firt name,last name: {} {}'.format(self.first_name,self.last_name))
        print('Balance: {}'.format(self.balance))

        

