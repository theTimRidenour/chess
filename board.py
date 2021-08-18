board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]

class Board:
    def add_piece(object):
        board[object.get_y()][object.get_x()] = object

    def remove_piece(object):
        board[object.get_y()][object.get_x()] = None

    def move_piece(object, new_x, new_y):
        Board.remove_piece(object)
        object.set_x(new_x)
        object.set_y(new_y)
        Board.add_piece(object)

    def display_board():
        for row in board:
            print(row)

    def draw_pieces():
        pass

