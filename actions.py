import board
import pieces

current_player = 'BLACK'
active_player = False
active_object = None

def action(player):
    global active_player
    global active_object
    if board.board[player.get_y()][player.get_x()] != None:
        current_object = board.board[player.get_y()][player.get_x()]
        if current_object.get_color() == current_player and not active_player:
            if current_object.get_moves() != []:
                for coor in current_object.get_moves():
                    x = current_object.get_x() + coor[0]
                    y = current_object.get_y() + coor[1]
                    board.move_board[y][x] = (x, y)
                    active_player = True
                    active_object = current_object
        elif active_player:
            print('oops')
            board.move_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
            active_player = False
            active_object = None
