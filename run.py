import random

print("----------------\nWelcome to tic-tac-toe!\n----------------\n")
print("You will play against of the computer, Good Luck 🙃\n")
print(
    "Rule:The player who succeeds in placing three of their marks in a\n horizontal, vertical, or diagonal row is the winner.\n"
)
print("You need choose one move on the board.\n This is the board.\n")
print("\n_ _ _")
print("_ _ _")
print("_ _ _\n")
print(


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
            board_positions.append('o')
        elif player_board & (1 << element):
            board_positions.append('x')
        else:
            board_positions.append(' ')
    print(board_string.format(*board_positions))
