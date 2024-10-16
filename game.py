import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

symbol_value = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

# Function to check if there are winning lines
def check_winning(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        won_line = True  # Assume the line is winning

        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                won_line = False
                break

        if won_line:  # If the line is indeed winning, calculate the winnings
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

# Function to simulate a spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Append symbols to all_symbols list
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    # Loop through columns and randomly choose symbols
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Function to print the slot machine in a grid format
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end='')

        print()

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

# Spin function to handle betting and spinning
def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. You need ${total_bet}, but your balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}. ")

    # Simulate and print the slot machine spin
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # Check if there are any winnings
    winnings, winnings_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won lines: ", *winnings_lines)

    # Update balance after winning or losing
    return winnings - total_bet


# Main function to run the betting process
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        play = input("Press enter to play (Q or q to quit): ")
        if play.lower() == 'q':
            break
        balance_change = spin(balance)
        balance += balance_change

    print(f"You left with ${balance}")


main()

# Resource get from -->  https://youtu.be/th4OBktqK1I