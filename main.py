MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

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


def main():
    balance = deposit()
    lines = get_number_of_lineS()
    print(balance, lines)

main()