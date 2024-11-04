def check_win(board, current_player, player_won, game_on, player1, player2):
    n = len(board)  # Get the size of the board
    win_length = 3  # Number of consecutive marks required to win

    # checking current player mark
    if current_player == player1:
        mark = "X"
    else:
        mark = "0"
    # Check rows for a win
    for row in range(n):
        for col in range(n - win_length + 1):  # Ensure we have enough cells left to check
            if all(board[row][col + k] == mark for k in range(win_length)):
                print(f"{current_player} WON by completing a row!")
                player_won += 1
                game_on = False
                return player_won, game_on

    # Check columns for a win
    for col in range(n):
        for row in range(n - win_length + 1):  # Ensure we have enough cells left to check
            if all(board[row + k][col] == mark for k in range(win_length)):
                print(f"{current_player} WON by completing a column!")
                player_won += 1
                game_on = False
                return player_won, game_on

    # Check main diagonals for a win
    for row in range(n - win_length + 1):
        for col in range(n - win_length + 1):
            if all(board[row + k][col + k] == mark for k in range(win_length)):
                print(f"{current_player} WON by completing a diagonal!")
                player_won += 1
                game_on = False
                return player_won, game_on

    # Check anti-diagonals for a win
    for row in range(n - win_length + 1):
        for col in range(win_length - 1, n):
            if all(board[row + k][col - k] == mark for k in range(win_length)):
                print(f"{current_player} WON by completing an anti-diagonal!")
                player_won += 1
                game_on = False
                return player_won, game_on

    return player_won, game_on


def find_location(nested_list, target):
    for row_index, row in enumerate(nested_list):
        for col_index, element in enumerate(row):
            if element == target:
                return row_index, col_index
    return None  # Return None if the target is not found

def create_board(board_size):
    # Initialize the board with numbered positions
    return [[(i * board_size + j + 1) for j in range(board_size)] for i in range(board_size)]

def display_board(board):
    board_size = len(board)
    max_width = len(str(board_size * board_size))

    board_str = ""
    for row in range(board_size):
        board_str += " | ".join(f"{cell:>{max_width}}" for cell in board[row]) + "\n"
        if row < board_size - 1:
            board_str += "-" * ((max_width + 3) * board_size - 3) + "\n"
    print(board_str)

def play(player1_name, player2_name, player1_won, player2_won, switch_player,board_size):
    # validate board size input
    try:
        board_size = int(board_size)
        board = create_board(board_size)
        position = [[0 for _ in range(board_size)] for _ in range(board_size)]  # Track positions

        turn_count = 0
        game_on = True

        while game_on:
            if turn_count == board_size * board_size:
                print("It's a Tie!")
                break

            # Display the current board
            display_board(board)

            # Determine current player
            current_player = player1_name if (turn_count % 2 == 0) ^ (switch_player % 2 != 0) else player2_name

            user_choice = input(f"Please choose a position, {current_player}: ")

            # Validate input
            try:
                user_choice = int(user_choice)
                location = find_location(board, user_choice)
                if location:
                    row, column = location
                    if position[row][column] == 0:
                        # Mark the board and track player positions
                        position[row][column] = 1
                        if current_player == player1_name:
                            board[row][column] = 'X'
                            player1_won, game_on = check_win(board, current_player, player1_won, game_on,player1_name,player2_name)
                        else:
                            board[row][column] = '0'
                            player2_won, game_on = check_win(board, current_player, player1_won, game_on,player1_name,player2_name)
                        turn_count += 1
                    else:
                        print("This position is already chosen.")
                else:
                    print("You inserted an invalid position.")
            except ValueError:
                print("You inserted an invalid input.")

        return player1_won, player2_won  # Return updated scores
    except ValueError:
        print("Please choose a numeric value")

def main():
    player_1 = input("Please input player 1 name: ")
    player_2 = input("Please input player 2 name: ")
    board_size = input("Please choose your board size: ")
    player1_won = 0
    player2_won = 0
    switch_starting_player = 0
    while True:
        player1_won, player2_won = play(player_1, player_2, player1_won, player2_won, switch_starting_player,board_size)
        to_continue = input("Do you want to continue Y/N: ").lower()
        if to_continue == "n":
            # Announce the winner or if it's a tie
            if player1_won > player2_won:
                print(f"{player_1} Score: {player1_won}, {player_2} Score: {player2_won}. {player_1} WON!!!!")
            elif player2_won > player1_won:
                print(f"{player_1} Score: {player1_won}, {player_2} Score: {player2_won}. {player_2} WON!!!!")
            else:
                print(f"{player_1} Score: {player1_won}, {player_2} Score: {player2_won}. It's a Tie!!!!")
            break
        else:
            print("Starting a new Game..........")
            switch_starting_player += 1
            continue

main()
