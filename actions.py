import board
import pieces

current_player = 'BLACK'
active_player = False
active_object = None

def action(player):
    global active_player
    global active_object
    global current_player
    if board.board[player.get_y()][player.get_x()] != None and not active_player:
        current_object = board.board[player.get_y()][player.get_x()]
        if current_object.get_color() == current_player and not active_player:
            if current_object.get_moves() != []:
                for coor in current_object.get_moves():
                    x = current_object.get_x() + coor[0]
                    y = current_object.get_y() + coor[1]
                    if board.board[y][x] == None:
                        board.move_board[y][x] = (x, y)
                        active_player = True
                        active_object = current_object
                    elif board.board[y][x].get_color() != current_player:
                        board.attack_board[y][x] = (x, y)
                        active_player = True
                        active_object = current_object
    elif board.board[player.get_y()][player.get_x()] == active_object:
        board.move_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        board.attack_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        active_player = False
        active_object = None
    
    elif board.move_board[player.get_y()][player.get_x()] != None:
        board.Board.move_piece(active_object, player.get_x(), player.get_y())
        board.move_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        board.attack_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        active_player = False
        active_object = None
        if current_player == 'BLACK':
            current_player = 'WHITE'
        else:
            current_player = 'BLACK'

    elif board.attack_board[player.get_y()][player.get_x()] != None:
        if board.board[player.get_y()][player.get_x()] not in pieces.removed_pieces:
            pieces.removed_pieces.append(board.board[player.get_y()][player.get_x()])
        board.Board.move_piece(active_object, player.get_x(), player.get_y())
        board.move_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        board.attack_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        active_player = False
        active_object = None
        if current_player == 'BLACK':
            current_player = 'WHITE'
        else:
            current_player = 'BLACK'
