import board
import pieces

current_player = 'BLACK'

def action(player):
    if board.board[player.get_y()][player.get_x()] != None:
        current_object = board.board[player.get_y()][player.get_x()]
        for coor in current_object.get_moves():
            x = current_object.get_x() + coor[0]
            y = current_object.get_y() + coor[1]
            board.move_board[y][x] = (x, y)