# Tic-Tac-Toe

A simple command-line Tic-Tac-Toe game implemented in Python. Two players take turns entering coordinates to place their markers until one wins by filling a row, column, or diagonal.

## Features

- Configurable board size (default is 3×3)
- Two-player turn-based play
- Win detection for rows, columns, and both diagonals
- Simple ASCII board display

## Prerequisites

- Python 3.x

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed:

   ```sh
   python3 --version
   ```

## Usage

1. Open a terminal and navigate to the directory containing `tic-tac-toe.py`.
2. Run the game:

   ```sh
   python3 tic-tac-toe.py
   ```

3. Follow the prompts:
   - Enter the X and Y coordinates (0-based) when prompted.
   - The board will display after each move.
   - The game ends when a player wins or the board is full.

## Example Play

```
Jordan's turn
Enter x coordinate: 0
Enter y coordinate: 0
x |   |  
---------
  |   |  
---------
  |   |  

Shubham's turn
Enter x coordinate: 1
Enter y coordinate: 1
x |   |  
---------
  | o |  
---------
  |   |  
...
Jordan wins!
```

## Code Overview

- **Player**: Represents a player with a name and marker (`x` or `o`).
- **Board**: Manages the game board, placement logic, and win detection.
- **Game**: Controls the turn sequence and user input loop.
- **printer**: Helper function to display the current board state.

## License

MIT License. Feel free to use and modify this code.# Tic-Tac-Toe

A simple command-line Tic-Tac-Toe game implemented in Python. Two players take turns entering coordinates to place their markers until one wins by filling a row, column, or diagonal.

## Features

- Configurable board size (default is 3×3)
- Two-player turn-based play
- Win detection for rows, columns, and both diagonals
- Simple ASCII board display

## Prerequisites

- Python 3.x

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed:

   ```sh
   python3 --version
   ```

## Usage

1. Open a terminal and navigate to the directory containing `tic-tac-toe.py`.
2. Run the game:

   ```sh
   python3 tic-tac-toe.py
   ```

3. Follow the prompts:
   - Enter the X and Y coordinates (0-based) when prompted.
   - The board will display after each move.
   - The game ends when a player wins or the board is full.

## Example Play

```
Jordan's turn
Enter x coordinate: 0
Enter y coordinate: 0
x |   |  
---------
  |   |  
---------
  |   |  

Shubham's turn
Enter x coordinate: 1
Enter y coordinate: 1
x |   |  
---------
  | o |  
---------
  |   |  
...
Jordan wins!
```

## Code Overview

- **Player**: Represents a player with a name and marker (`x` or `o`).
- **Board**: Manages the game board, placement logic, and win detection.
- **Game**: Controls the turn sequence and user input loop.
- **printer**: Helper function to display the current board state.

## License

MIT License. Feel free to use and modify this code.
