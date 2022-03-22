import random
import time

# board game


def print_board(computer_board, player_board):

    """
    Main function for print the board.
    """
    board_string = """
    {0} | {1} | {2}
    -----------
    {3} | {4} | {5}
    -----------
    {6} | {7} | {8}
     """
    board_positions = []
    for element in range(0, 9):
        if computer_board & (1 << element):
            board_positions.append("o")
        elif player_board & (1 << element):
            board_positions.append("x")
        else:
            board_positions.append(" ")
    print(board_string.format(*board_positions))


# decide who goes first with the coin flip function
def who_goes_first():

    """
    Fuction to flip a coin to decide who go first.
    """
    coin_choice = validate_and_input(
        "To decide who goes first,lets flip a coin, (h)eads or (t)ails?",
        ["h", "t"]
        )
    print("flipping coin...\n")
    time.sleep(1)
    if (random.randint(0, 2) == 1 and coin_choice == "h") or (
        random.randint(0, 2) == 0 and coin_choice == "t"
    ):
        print("Good guess, you go first!\n")
        return True
    else:
        print("Better luck next time, computer goes first\n")
        return False

# sleep funtion so the game do not run so fast


def sleep_input(string):
    """
   function to slow down the game.
    """
    input_str = input(string)
    time.sleep(0.5)
    return input_str


# check if data on input is valid.
def validate_and_input(string, valid_input):

    """
    Funtion to check if data is valid.
    """
    input = '----'
    while input not in valid_input:
        input = sleep_input(string)
    return input


# ask for player move.
def get_player_move():
    """
Function to aask the player move.
    """
    return int(validate_and_input("""Choose your move 0,1,2
                 3,4,5
                 6,7,8\n""", ['0', '1', '2', '3', '4', '5', '6', '7', '8']))


# mark player move on the board.

def player_move(computer_board, player_board, player_move):
    """
    fuction to mark player move
    """
    if not computer_board & (1 << player_move) and not player_board & (
            1 << player_move):
        return player_board | (1 << player_move), True
    else:
        return None, False


# Defines the computer move randon.

def get_computer_moveset():
    """
    Funtion to define the computer move random
    """
    computer_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(computer_moves)
    return computer_moves


# function to define computer move on the board.

def computer_move(computer_moves, player_board, computer_board):
    """
 Define and mark move on the computer board.
    """
    print("computer is thinking...")
    time.sleep(3)
    while len(computer_moves) > 0:
        computer_move = computer_moves.pop()
        if not player_board & (1 << computer_move):
            return computer_board | (1 << computer_move), computer_moves
    return computer_board, computer_moves

# check  fot win funtion.


def check_win(win_conditions, computer_board, player_board):
    """
    Fuction check for win or tie using bit manipulation.
    """
    for win_condition in win_conditions:
        if win_condition & player_board == win_condition:
            return "player"
        elif win_condition & computer_board == win_condition:
            return "computer"
        elif computer_board & player_board == 0b111111111:
            return "tie"
    return ""

# constant for win fuction usin bit manipulation.


def get_constants():
    """
    Fuction for win moves using bit manipulation.
    """
    return 0, 0, [0b111000000,
                  0b000111000,
                  0b000000111,
                  0b100100100,
                  0b010010010,
                  0b001001001,
                  0b100010001,
                  0b001010100], get_computer_moveset()

# board after player move.


def get_player_board_after_move(computer_board, player_board):
    """
 Show board uptaded after player move.
    """
    success = False
    while not success:
        move = get_player_move()
        temp, success = player_move(computer_board, player_board, move)
    return temp


def check_and_act_on_end_conditions
 (player_board, computer_board, win_conditions):
    """
    Print messages if the game finish and check condion.
    """
    condition = check_win(win_conditions, computer_board, player_board)
    if condition == '':
        return False
    if condition == "tie":
        print("DRAW! Almost, but not quite 😐")
    if condition == "player":
        print("Ayyy, you won! Nice one 😊")
    if condition == "computer":
        print("You got beaten, damn 💩")
    return True

# main fuction to call the anothers fuction and while loop.


def main():
    print("----------------\nWelcome to tic-tac-toe!\n----------------\n")
    print("You will play against of the computer, Good Luck 👍\n")
    print("Rule: The player who succeeds in placing three of their marks in a
          horizontal, vertical, or diagonal row is the winner.\n")
    print("You need choose one move on the board.\n
          This is how the board looks.\n")
    print("\n_ _ _")
    print("_ _ _")
    print("_ _ _\n")
    player_board, computer_board, win_conditions,
    computer_moves = get_constants()
    is_player_turn = who_goes_first()
    finished = False
    while not finished:
        if is_player_turn:
            player_board = get_player_board_after_move
            (computer_board, player_board)
        else:
            computer_board, computer_moves = computer_move
            (computer_moves, player_board, computer_board)
        print_board(computer_board, player_board)
        is_player_turn = not is_player_turn
        finished = check_and_act_on_end_conditions
        (player_board, computer_board, win_conditions)


if __name__ == '__main__':
    main()
