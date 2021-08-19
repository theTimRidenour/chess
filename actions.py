import board
import pieces

current_player = 'BLACK'

def action(player):
    if board.board[player.get_y()][player.get_x()] != None:
        current_object = board.board[player.get_y()][player.get_x()]
        print(current_object.get_color())