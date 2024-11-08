
# Tic-Tac-Toe Game (Customizable Board Size)

This is a Python-based implementation of Tic-Tac-Toe that allows players to play on a custom-sized board (3x3, 4x4, etc.) and requires three consecutive marks to win. The game supports two players and tracks their scores across multiple rounds.

## Features

- **Customizable Board Size**: Players can select the board size at the beginning of the game.
- **Search Option**:It's search for a win check depending on last insert data position instead of whole array.********
- **Win Detection**: The game detects a win when a player marks three consecutive cells in a row, column, or diagonal, regardless of board size.
- **Score Tracking**: Scores are tracked across multiple rounds, and players can play as many rounds as they like.
- **Tie Detection**: The game announces a tie if all cells are marked without any player winning.
- **Alternating Turns**: Players take turns marking cells, with a toggle option to switch the starting player for each round.

## How to Play

1. **Run the Game**: Start the game by running the `main()` function.
2. **Enter Player Names**: Input names for both players.
3. **Choose Board Size**: Enter a numeric board size, e.g., `3` for a 3x3 board.
4. **Take Turns**: Players take turns selecting board positions by entering numbers corresponding to unmarked cells.
5. **Win Condition**: Win by marking three consecutive cells in any row, column, or diagonal.
6. **Continue or Exit**: After each round, choose whether to continue or exit. Scores will be displayed at the end.

## Code Files

- `main()`: Starts the game and allows players to input names and board size.
- `create_board(board_size)`: Creates a board with numbered positions.
- `display_board(board)`: Displays the current state of the board.
- `find_location(nested_list, target)`: Finds the row and column of a specific cell on the board.
- `check_win(board, current_player, player_won, game_on, player1, player2)`: Checks if a player has won by completing three consecutive cells in a row, column, or diagonal.
- `play(player1_name, player2_name, player1_won, player2_won, switch_player, board_size)`: Manages the core gameplay loop and handles player turns.

## Example Output

```
Please input player 1 name: Alice
Please input player 2 name: Bob
Please choose your board size: 3

 | 1 | 2 | 3
-----------
 | 4 | 5 | 6
-----------
 | 7 | 8 | 9

Please choose a position, Alice: 5
Alice WON by completing a row!
Starting a new Game..........
```

## Requirements

This script requires **Python 3.x** and no additional libraries.

## License

This project is licensed under the MIT License.
