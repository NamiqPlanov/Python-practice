from game import *

def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print('you do not have  enough money to bet. your current balance is {}$'.format(balance))
        else:
            break
    print('You are beting {}$ on {} lines. Your total bet is {}'.format(bet,lines,total_bet))

    slots = get_machine_spin(rows_num,col_num,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print('You won {}$'.format(winnings))
    print('You won on:',*winning_lines)
main()

