
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+"): ")
        # lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please Enter a number.")

    return lines

def get_bet():
    while True:
        bet_amount = input("What would you like to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")

    return bet_amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()

    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet} ")


main()

# https://youtu.be/th4OBktqK1I