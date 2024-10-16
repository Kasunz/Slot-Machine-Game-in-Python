# Slot Machine Game in Python

This is a simple text-based slot machine game implemented in Python. The user can deposit money, place bets on a specified number of lines, and then spin the slot machine to try their luck. The game provides winnings based on matching symbols on the specified number of lines.

## Features

- **Deposit Money**: The player can deposit a custom amount of money to start the game.
- **Betting**: The player can place bets on 1 to 3 lines and specify a custom bet amount.
- **Slot Machine Spin**: The slot machine will randomly generate symbols across three rows and three columns.
- **Winnings**: The player wins if any of the lines they bet on have matching symbols. The amount won is based on the value of the symbols and the amount bet.

## How to Run

1. Clone or download the repository.
2. Ensure you have Python installed.
3. Run the script:

```bash
python slot_machine.py
```

## How It Works

1. **Deposit Money**:  
   The player is asked to deposit a custom amount of money to start the game. The deposit must be a positive integer.

2. **Place a Bet**:  
   The player selects how many lines (1-3) they want to bet on. Then, the player is prompted to enter a bet amount for each line. The total bet is calculated as `bet amount * number of lines`.

3. **Spin the Slot Machine**:  
   The slot machine generates random symbols for each row and column. The possible symbols are `'A'`, `'B'`, `'C'`, and `'D'`, each having a different occurrence probability.

4. **Check for Winnings**:  
   The player wins if the symbols in any of the lines they bet on match across all columns. The value of the symbols determines how much they win.

5. **Repeat or Quit**:  
   The player can continue playing as long as they have money left. They can quit the game at any time by pressing `Q` or `q`.



## Example Playthrough

```
Enter the amount you'd like to deposit: $100
Current balance is $100
Press enter to play (Q or q to quit): 
Enter the number of lines to bet on (1-3): 2
Enter the bet amount per line (between $1 and $100): $20
You are betting $20 on 2 lines. Total bet: $40. 
D | B | C
C | C | C
C | D | B
You won $60!
You won lines:  2
Current balance is $120
Press enter to play (Q or q to quit): q
You left with $120
```

## Project Structure

- `slot_machine.py`: The main Python script containing the game logic.
- README.md: This file, providing instructions and details for the game.

## License

This project is for educational purposes and does not come with any specific license.
