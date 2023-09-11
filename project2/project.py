import random

MAX_LINES = 4
MAX_BET = 150
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A':2,
    'B':4,
    'C':6,
    'D':8

}

def get_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in (rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)


        

def deposit():
    while True:
        amount =input('what will be your deposit?$')
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print('number must be greater than 0.')
        else:
            print('Enter a number please')

    return amount

def get_lines():
    while True:
        lines =input('Enter number of lines to bet on.(1-{})'.format(str(MAX_LINES)))
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print('Enter vaid number')
        else:
            print('Enter a number please')

    return lines

def get_bet():
    while True:
        amount = input('What will be your bet?')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print('Amount must be between {} and {}'.format(MIN_BET,MAX_BET))
        else:
            print('Enter a number')

def main():
    balance = deposit()
    lines_main = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines_main
        if total_bet>balance:
            print('You do not have enough money to bet.Your balance is ${}'.format(balance))
        else:
            break
    
    print('You are betting {}$ on {} lines.Your total bet is {}'.format(bet,lines_main,total_bet))
main()
       

