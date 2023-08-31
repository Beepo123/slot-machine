import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "S": 1,
    "A": 2,
    "B": 4,
    "C": 8,
}


def deposit():
    # ask user for valid amount value
    while True:
        amount = input("Enter amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
        else:
            print("Enter a number: ")

    return amount


def get_number_of_lineS():
    # ask user for number of lines to bet
    while True:
        lines = input(f"Enter number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if lines >= 1 and lines <= MAX_LINES:
                break
        else:
            print("Enter valid number: ")

    return lines


def get_bet(balance, lines):
    # ask user for amount of bet
    # if bet > balance, ask again
    while True:
        bet_amount = input("What would you like that to bet on each line: ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                if bet_amount * lines <= balance:
                    break
                else:
                    print("Not enough balance")
            else:
                print(f"Enter a bet between {MIN_BET} - {MAX_BET}: ")
        else:
            print("Please enter a number")

    return bet_amount


def main():
    balance = deposit()
    lines = get_number_of_lineS()
    bet = get_bet(balance, lines)
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")


main()
