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
        "To decide who goes first, lets flip a coin, (h)eads or (t)ails?", ["h", "t"]
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


def sleep_input(string):
    input_str = input(string)
    time.sleep(0.5)
    return input_str


# check if data on input is valid 
def validate_and_input(string, valid_input):

    """
    Funtion to check if data is valid 
    """
    input = '----'
    while input not in valid_input:
        input = sleep_input(string)
    return input


# ask for player move 
def get_player_move():
    return int(validate_and_input("""Choose your move 0,1,2
                 3,4,5
                 6,7,8\n""", ['0', '1', '2', '3', '4', '5', '6', '7', '8']))


def main():
    print("----------------\nWelcome to tic-tac-toe!\n----------------\n")
    print("You will play against of the computer, Good Luck 🙃\n")
    print(
        "Rule: The player who succeeds in placing three of their marks in a\n horizontal, vertical, or diagonal row is the winner.\n"
    )
    print("You need choose one move on the board.\n This is how the board looks.\n")
    print("\n_ _ _")
    print("_ _ _")
    print("_ _ _\n")
