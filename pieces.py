import board
import graphics

color = ('BLACK', 'WHITE')
cnt = 1
removed_pieces = []

class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, window, x, y):
        window.blit(self.img, (x, y))

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_image(self):
        return self.img

class King:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window, x, y):
        window.blit(self.img, (x, y))

    def set_has_moved(self, b):
        self.has_moved = b

    def get_moves(self):
        moves = []
        if self.x == 4 and not self.has_moved:
            if board.board[self.y][self.x -3] == None and board.board[self.y][self.x -2] == None and board.board[self.y][self.x -1] == None and isinstance(board.board[self.y][self.x - 4], (Rook)):
                    moves.append((-2, 0, True))
            if board.board[self.y][self.x +1] == None and board.board[self.y][self.x +2] == None and isinstance(board.board[self.y][self.x + 3], (Rook)):
                    moves.append((2, 0, True))
        if self.x > 0:
            moves.append((-1, 0))
            if self.y > 0:
                moves.append((-1, -1))
        if self.x < 7:
            moves.append((1, 0))
            if self.y < 7:
                moves.append((1, 1))
        if self.y > 0:
            moves.append((0, -1))
            if self.x < 7:
                moves.append((1, -1))
        if self.y < 7:
            moves.append((0, 1))
            if self.x > 0:
                moves.append((-1, 1))

        return moves

    def get_has_moved(self):
        return self.has_moved

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def get_image(self):
        return self.img

class Queen:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def set_has_moved(self, b):
        self.has_moved = b

    def get_moves(self):
        moves = []
        if self.x > 0:
            i = 1
            while i <= self.x:
                moves.append((-i, 0))
                if board.board[self.y][self.x - i] != None:
                    break
                else:
                    i += 1
            if self.y > 0:
                i = 1
                while i <= self.x and i <= self.y:
                    moves.append((-i, -i))
                    if board.board[self.y - i][self.x - i] != None:
                        break
                    else:
                        i += 1
        if self.x < 7:
            i = self.x + 1
            while i <= 7:
                moves.append((i - self.x, 0))
                if board.board[self.y][i] != None:
                    break
                else:
                    i += 1
            if self.y < 7:
                i = self.x + 1
                j = self.y + 1
                while i <= 7 and j <= 7:
                    moves.append((i - self.x, j - self.y))
                    if board.board[j][i] != None:
                        break
                    else:
                        i += 1
                        j += 1
        if self.y > 0:
            i = 1
            while i <= self.y:
                moves.append((0, -i))
                if board.board[self.y - i][self.x] != None:
                    break
                else:
                    i += 1
            if self.x < 7:
                i = self.x + 1
                j = 1
                while j <= self.y and i <= 7:
                    moves.append((i - self.x, -j))
                    if board.board[self.y - j][i] != None:
                        break
                    else:
                        i += 1
                        j += 1
        if self.y < 7:
            i = self.y + 1
            while i <= 7:
                moves.append((0, i - self.y))
                if board.board[i][self.x] != None:
                    break
                else:
                    i += 1
            if self.x > 0:
                i = 1
                j = self.y + 1
                while i <= self.x and j <= 7:
                    moves.append((-i, j - self.y))
                    if board.board[j][self.x - i] != None:
                        break
                    else:
                        i += 1
                        j += 1
        return moves

    def get_special_moves(self):
        moves = {}
        #if not self.has_moved:
        #    for rook in rooks:
        #        if rook.get_color == self.get_color and not rook.get_has_moved:
        #            if rook.get_x < self.get_x:
        #                moves += {(self, (0, -2)): (rook, (0, 3))}
        #            else:
        #                moves += {(self, (0, 2)): (rook, 0, -2)}
        return moves

    def get_has_moved(self):
        return self.has_moved

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def get_image(self):
        return self.img

class Bishop:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def set_has_moved(self, b):
        self.has_moved = b

    def get_moves(self):
        moves = []
        if self.x > 0 and self.y > 0:
            i = 1
            while i <= self.x and i <= self.y:
                moves.append((-i, -i))
                if board.board[self.y - i][self.x - i] != None:
                    break                    
                else:
                    i += 1
        if self.x < 7 and self.y < 7:
            i = self.x + 1
            j = self.y + 1
            while i <= 7 and j <= 7:
                moves.append((i - self.x, j - self.y))
                if board.board[j][i] != None:
                    break
                else:
                    i += 1
                    j += 1
        if self.y > 0 and self.x < 7:
            i = self.x + 1
            j = 1
            while j <= self.y and i <= 7:
                moves.append((i - self.x, -j))
                if board.board[self.y - j][i] != None:
                    break
                else:
                    i += 1
                    j += 1
        if self.y < 7 and self.x > 0:
            i = 1
            j = self.y + 1
            while i <= self.x and j <= 7:
                moves.append((-i, j - self.y))
                if board.board[j][self.x - i] != None:
                    break
                else:
                    i += 1
                    j += 1
        return moves

    def get_has_moved(self):
        return self.has_moved

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def get_image(self):
        return self.img

class Knight:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def set_has_moved(self, b):
        self.has_moved = b

    def get_moves(self):
        moves = []
        if self.x - 2 >= 0:
            if self.y - 1 >= 0:
                moves.append((-2, -1))
            if self.y + 1 <= 7:
                moves.append((-2, 1))
        if self.x + 2 <= 7:
            if self.y - 1 >= 0:
                moves.append((2, -1))
            if self.y + 1 <= 7:
                moves.append((2, 1))
        if self.y - 2 >= 0:
            if self.x - 1 >= 0:
                moves.append((-1, -2))
            if self.x + 1 <= 7:
                moves.append((1, -2))
        if self.y + 2 <= 7:
            if self.x - 1 >= 0:
                moves.append((-1, 2))
            if self.x + 1 <= 7:
                moves.append((1, 2))
        return moves

    def get_has_moved(self):
        return self.has_moved

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def get_image(self):
        return self.img

class Rook:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def set_has_moved(self, b):
        self.has_moved = b

    def get_moves(self):
        moves = []
        if self.x > 0:
            i = 1
            while i <= self.x:
                moves.append((-i, 0))
                if board.board[self.y][self.x - i] != None:
                    break
                else:
                    i += 1
        if self.x < 7:
            i = self.x + 1
            while i <= 7:
                moves.append((i - self.x, 0))
                if board.board[self.y][i] != None:
                    break
                else:
                    i += 1
        if self.y > 0:
            i = 1
            while i <= self.y:
                moves.append((0, -i))
                if board.board[self.y - i][self.x] != None:
                    break
                else:
                    i += 1
        if self.y < 7:
            i = self.y + 1
            while i <= 7:
                moves.append((0, i - self.y))
                if board.board[i][self.x] != None:
                    break
                else:
                    i += 1
        return moves

    def get_has_moved(self):
        return self.has_moved

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def get_image(self):
        return self.img

class Pawn:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def convert_pawn(self):
        global cnt
        name = 'p' + str(cnt)
        cnt += 1
        if self.color == 'BLACK':
            img = graphics.BLACK_QUEEN
        else:
            img = graphics.WHITE_QUEEN
        globals()[name] = Queen(self.color, self.x, self.y, img)
        board.board[self.y][self.x] = globals()[name]

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def set_has_moved(self, b):
        self.has_moved = b

    def get_moves(self):
        moves = []
        a = 1
        if self.color == 'WHITE':
            a = -1
        if (self.y == 1 or self.y == 6) and not self.has_moved:
            if board.board[self.y + (a * 2)][self.x] == None and board.board[self.y + a][self.x] == None:
                moves.append((0, a * 2))
        if (self.y > 0 and self.color == 'WHITE') or (self.y < 7 and self.color == 'BLACK'):
            if board.board[self.y + a][self.x] == None:
                moves.append((0, a))
            if self.x - 1 >= 0:
                if board.board[self.y + a][self.x - 1] != None:
                    if (a == 1 and board.board[self.y + a][self.x - 1].color == 'WHITE') or (a == -1 and board.board[self.y + a][self.x - 1].color == 'BLACK'):
                        moves.append((-1, a))
            if self.x + 1 <= 7:
                if board.board[self.y + (a)][self.x + 1] != None:
                    if (a == 1 and board.board[self.y + a][self.x + 1].color == 'WHITE') or (a == -1 and board.board[self.y + a][self.x + 1].color == 'BLACK'):
                        moves.append((1, a))
        return moves

    def get_has_moved(self):
        return self.has_moved

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_color(self):
        return self.color

    def get_image(self):
        return self.img

def load_pieces(graphics):
    bd = board.Board
    white_king =    King  (color[1], 4, 7, graphics.WHITE_KING)
    white_queen =   Queen (color[1], 3, 7, graphics.WHITE_QUEEN)
    white_bishop1 = Bishop(color[1], 5, 7, graphics.WHITE_BISHOP)
    white_bishop2 = Bishop(color[1], 2, 7, graphics.WHITE_BISHOP)
    white_knight1 = Knight(color[1], 6, 7, graphics.WHITE_KNIGHT)
    white_knight2 = Knight(color[1], 1, 7, graphics.WHITE_KNIGHT)
    white_rook1 =   Rook  (color[1], 7, 7, graphics.WHITE_ROOK)
    white_rook2 =   Rook  (color[1], 0, 7, graphics.WHITE_ROOK)
    white_pawn1 =   Pawn  (color[1], 0, 6, graphics.WHITE_PAWN)
    white_pawn2 =   Pawn  (color[1], 1, 6, graphics.WHITE_PAWN)
    white_pawn3 =   Pawn  (color[1], 2, 6, graphics.WHITE_PAWN)
    white_pawn4 =   Pawn  (color[1], 3, 6, graphics.WHITE_PAWN)
    white_pawn5 =   Pawn  (color[1], 4, 6, graphics.WHITE_PAWN)
    white_pawn6 =   Pawn  (color[1], 5, 6, graphics.WHITE_PAWN)
    white_pawn7 =   Pawn  (color[1], 6, 6, graphics.WHITE_PAWN)
    white_pawn8 =   Pawn  (color[1], 7, 6, graphics.WHITE_PAWN)

    black_king =    King  (color[0], 4, 0, graphics.BLACK_KING)
    black_queen =   Queen (color[0], 3, 0, graphics.BLACK_QUEEN)
    black_bishop1 = Bishop(color[0], 5, 0, graphics.BLACK_BISHOP)
    black_bishop2 = Bishop(color[0], 2, 0, graphics.BLACK_BISHOP)
    black_knight1 = Knight(color[0], 6, 0, graphics.BLACK_KNIGHT)
    black_knight2 = Knight(color[0], 1, 0, graphics.BLACK_KNIGHT)
    black_rook1 =   Rook  (color[0], 7, 0, graphics.BLACK_ROOK)
    black_rook2 =   Rook  (color[0], 0, 0, graphics.BLACK_ROOK)
    black_pawn1 =   Pawn  (color[0], 0, 1, graphics.BLACK_PAWN)
    black_pawn2 =   Pawn  (color[0], 1, 1, graphics.BLACK_PAWN)
    black_pawn3 =   Pawn  (color[0], 2, 1, graphics.BLACK_PAWN)
    black_pawn4 =   Pawn  (color[0], 3, 1, graphics.BLACK_PAWN)
    black_pawn5 =   Pawn  (color[0], 4, 1, graphics.BLACK_PAWN)
    black_pawn6 =   Pawn  (color[0], 5, 1, graphics.BLACK_PAWN)
    black_pawn7 =   Pawn  (color[0], 6, 1, graphics.BLACK_PAWN)
    black_pawn8 =   Pawn  (color[0], 7, 1, graphics.BLACK_PAWN)

    bd.add_piece(white_king)
    bd.add_piece(white_queen)
    bd.add_piece(white_bishop1)
    bd.add_piece(white_bishop2)
    bd.add_piece(white_knight1)
    bd.add_piece(white_knight2)
    bd.add_piece(white_rook1)
    bd.add_piece(white_rook2)
    bd.add_piece(white_pawn1)
    bd.add_piece(white_pawn2)
    bd.add_piece(white_pawn3)
    bd.add_piece(white_pawn4)
    bd.add_piece(white_pawn5)
    bd.add_piece(white_pawn6)
    bd.add_piece(white_pawn7)
    bd.add_piece(white_pawn8)
    bd.add_piece(black_king)
    bd.add_piece(black_queen)
    bd.add_piece(black_bishop1)
    bd.add_piece(black_bishop2)
    bd.add_piece(black_knight1)
    bd.add_piece(black_knight2)
    bd.add_piece(black_rook1)
    bd.add_piece(black_rook2)
    bd.add_piece(black_pawn1)
    bd.add_piece(black_pawn2)
    bd.add_piece(black_pawn3)
    bd.add_piece(black_pawn4)
    bd.add_piece(black_pawn5)
    bd.add_piece(black_pawn6)
    bd.add_piece(black_pawn7)
    bd.add_piece(black_pawn8)
