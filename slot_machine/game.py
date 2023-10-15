import random

max_lines = 4
max_bet = 150
min_bet = 1
rows_num = 3
col_num = 3

symbol_count = {
    'A':2,
    'B':4,
    'C':6,
    'D':8
}
symbol_values = {
    'A':5,
    'B':4,
    'C':3,
    'D':2
}



def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_check = column[line]
            if symbol!=symbol_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winning_lines,winnings


def get_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            columns.append(column)
    return columns


def print_slot_machine(columns):
    n = len(columns[0])
    for row in range(n):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end = ' | ')
            else:
                print(column[row],end = '')
        print()





def deposit():
    while True:
        amount = input('What will be your deposit?')
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print('number must be greater than 0')
    else:
        print('enter a number please')



def get_lines():
    while True:
        lines = input('Input number of lines to bet on.(1-{})'.format(str(max_lines)))
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=max_lines:
                break
            else:
                print('Enter a valid number')
        else:
            print('Enter a number please')
    return lines
def get_bet():
    while True:
        amount = input('What will be your bet?')
        if amount.isdigit():
            amount = int(amount)
            if min_bet<=amount<=max_bet:
                return amount
            else:
                print('Amount must be between {} and {}'.format(min_bet,max_bet))
        else:
            print('Enter a number')
