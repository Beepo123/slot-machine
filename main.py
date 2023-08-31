import random

MAX_LINES = 3
MAX_BET = 1_000_000
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "S": 1,
    "A": 2,
    "B": 4,
    "C": 8,
}


def spin_slot_machine(ROWS, COLS, symbols):
    slot_machine = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    # for each COL spin machine ROW times
    for i in range(COLS):
        # for each COL reset all odds
        symbols_copy = dict(symbols)
        for j in range(ROWS):
            # pick symbol from the list and add it to the machine result
            random_key = random.choices(list(symbols_copy.keys()), weights=list(symbols_copy.values()), k=1)
            random_key = random_key[0]
            slot_machine[i][j] = random_key

            # subtract the odds of the chosen key for the next spin
            # if odds becomes 0 delete the item from dictionary
            symbols_copy[random_key] -= 1
            if symbols_copy[random_key] == 0:
                del symbols_copy[random_key]

    return slot_machine


def print_slot_machine(slot_machine):
    pass


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


def get_number_of_lines():
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
    lines = get_number_of_lines()
    bet = get_bet(balance, lines)
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}")
    slot_machine = spin_slot_machine(ROWS, COLS, symbol_count)

    result = []
    for i in range(len(slot_machine[0])):
        temp = []
        for j in range(len(slot_machine)):
            print(slot_machine[i][j], end=" ")
            temp.append(slot_machine[i][j])
        result.append(temp)
        print("")
    
    print(result)
main()
