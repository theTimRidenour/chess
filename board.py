board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
player_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
move_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
attack_board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]

class Board:
    def add_piece(object):
        board[object.get_y()][object.get_x()] = object

    def add_player(object):
        player_board[object.get_y()][object.get_x()] = object

    def remove_piece(object):
        board[object.get_y()][object.get_x()] = None

    def remove_player(object):
        player_board[object.get_y()][object.get_x()] = None

    def move_piece(object, new_x, new_y):
        Board.remove_piece(object)
        object.set_x(new_x)
        object.set_y(new_y)
        Board.add_piece(object)

    def move_player(object, new_x, new_y):
        Board.remove_player(object)
        object.set_x(new_x)
        object.set_y(new_y)
        Board.add_player(object)

    def draw_pieces(window):
        for row in board:
            for piece in row:
                if piece != None:
                    window.blit(piece.get_image(), (int(piece.get_x() * 93.75), int(piece.get_y() * 93.75)))

    def draw_player(window, player):
        window.blit(player.get_image(), (int(player.get_x() * 93.75), int(player.get_y() * 93.75)))

    def draw_safe_squares(window, img_not_occ):
        for row in move_board:
            for square in row:
                if square != None:
                    window.blit(img_not_occ, (int(square[0] * 93.75), int(square[1] * 93.75)))
    
    def draw_attack_squares(window, img_not_occ):
        for row in attack_board:
            for square in row:
                if square != None:
                    window.blit(img_not_occ, (int(square[0] * 93.75), int(square[1] * 93.75)))
                    