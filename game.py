
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Function to handle the deposit
def deposit():
    while True:
        amount = input("Enter the amount you'd like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print("Invalid input! Please enter a number.")

    return amount

# Function to get the number of lines to bet on
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
            print("Invalid input! Please enter a number.")

    return lines

# Function to get the bet amount
def get_bet():
    while True:
        bet_amount = input(f"Enter the bet amount per line (between ${MIN_BET} and ${MAX_BET}): $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number")

    return bet_amount

# Main function to run the betting process
def main():
    balance = deposit()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. You need ${total_bet}, but your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}. ")


main()

# https://youtu.be/th4OBktqK1I