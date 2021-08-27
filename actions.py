import board
import pieces

from copy import copy, deepcopy

current_player = 'BLACK'
active_player = False
active_object = None
black_king_obj = None
white_king_obj = None

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
                        if len(coor) != 3:
                            board.move_board[y][x] = (x, y)
                        else:
                            board.move_board[y][x] = (x, y, True)
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
        if isinstance(active_object, (pieces.King)) and abs(player.get_x() - active_object.get_x()) == 2:
            if player.get_x() < active_object.get_x():
                board.Board.move_piece(board.board[active_object.get_y()][active_object.get_x() - 4], player.get_x() + 1, player.get_y())
            else:
                board.Board.move_piece(board.board[active_object.get_y()][active_object.get_x() + 3], player.get_x() - 1, player.get_y())
        board.Board.move_piece(active_object, player.get_x(), player.get_y())
        board.move_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        board.attack_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
        active_player = False
        active_object.set_has_moved(True)
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
        active_object.set_has_moved(True)
        active_object = None
        if current_player == 'BLACK':
            current_player = 'WHITE'
        else:
            current_player = 'BLACK'

    check_pawns()
    check = check_for_check()
    if check[0]:
        if check[1] != None:
            if check_for_checkmate(check[1]):
                print ('Checkmate:', check[1])
                globals()['run'] = False
            else:
                print('Check:', check[1])


def check_pawns():
    for object in board.board[0]:
        if isinstance(object, pieces.Pawn):
            object.convert_pawn()
    for object in board.board[7]:
        if isinstance(object, pieces.Pawn):
            object.convert_pawn()

def check_for_check(brd = board.board, king = None):
    if not kings_identitfied():
        return None
    # check if black king is in check
    if black_king_obj != None and (king == None or king == 'BLACK'):
        if black_king_obj.check(brd):
            return [True, 'BLACK']
    if white_king_obj != None and (king == None or king == 'WHITE'):
        if white_king_obj.check(brd):
            return [True, 'WHITE']
    return [False, None]
    
def check_for_checkmate(king = None):
    if king != None:
        x_val = black_king_obj.get_x() if king == 'BLACK' else white_king_obj.get_x()
        y_val = black_king_obj.get_y() if king == 'BLACK' else white_king_obj.get_y()
        BLACK_pieces = []
        WHITE_pieces = []
        for row in board.board:
            for object in row:
                if object != None:
                    BLACK_pieces.append(object) if object.get_color() == 'BLACK' else WHITE_pieces.append(object)
        possible_block = []
        opp_king = 'WHITE' if king == 'BLACK' else 'BLACK'

        for obj in locals()[opp_king + '_pieces']:
            if isinstance(obj, (pieces.Knight)):
                if x_val == (obj.get_x() - 2):
                    if y_val == (obj.get_y() - 1):
                        possible_block.append((obj.get_x(), obj.get_y()))
                    if y_val == (obj.get_y() + 1):
                        possible_block.append((obj.get_x(), obj.get_y()))
                elif x_val == (obj.get_x() - 1):
                    if y_val == (obj.get_y() - 2):
                        possible_block.append((obj.get_x(), obj.get_y()))
                    if y_val == (obj.get_y() + 2):
                        possible_block.append((obj.get_x(), obj.get_y()))
                elif x_val == (obj.get_x() + 1):
                    if y_val == (obj.get_y() - 2):
                        possible_block.append((obj.get_x(), obj.get_y()))
                    if y_val == (obj.get_y() + 2):
                        possible_block.append((obj.get_x(), obj.get_y()))
                elif x_val == (obj.get_x() + 2):
                    if y_val == (obj.get_y() - 1):
                        possible_block.append((obj.get_x(), obj.get_y()))
                    if y_val == (obj.get_y() + 1):
                        possible_block.append((obj.get_x(), obj.get_y()))
        print(possible_block)

        for checking_block in locals()[king + '_pieces']:
            checking_list = checking_block.get_moves()
            for poss_move in checking_list:
                pm_x = checking_block.get_x() + poss_move[0]
                pm_y = checking_block.get_y() + poss_move[1]
                for pb_x, pb_y in possible_block:
                    if pb_x == pm_x and pb_y == pm_y:
                        print (checking_block)
                        return False

        return True

#    double_check = check_for_check(board.board, king)
#    if double_check[0] == True:
#        cnt = 1
#        obj_list = []
#        checkmate_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
#        for row in board.board:
#            for object in row:
#                if object != None:
#                    locals()['obj' + str(cnt)] = copy(object)
#                    checkmate_board[object.get_y()][object.get_x()] = locals()['obj' + str(cnt)]
#                    if locals()['obj' + str(cnt)].get_color() == king:
#                        obj_list.append(locals()['obj' + str(cnt)])
#                    cnt += 1
#        for obj in obj_list:
#            check_moves = obj.get_moves()
#            for check_move in check_moves:
#                checkmove_board = checkmate_board[:]
#                checkmove_board[obj.get_y() + check_move[1]][obj.get_x() + check_move[0]] = obj
#                obj.set_x(obj.get_x() + check_move[0])
#                obj.set_y(obj.get_y() + check_move[1])
#                checkmove_board[obj.get_y()][obj.get_x()] = None
#                if check_for_check(checkmove_board, king)[0]:
#                    return False
#                obj.set_x(obj.get_x() - check_move[0])
#                obj.set_y(obj.get_y() - check_move[1])
#        return True
#    return False

def kings_identitfied():
    global black_king_obj, white_king_obj
    black_king_obj, white_king_obj = None, None
    for row in board.board:
        for object in row:
            if object != None:
                if isinstance(object, (pieces.King)):
                    if object.color == 'BLACK':
                        black_king_obj = object
                    else:
                        white_king_obj = object

    return True

