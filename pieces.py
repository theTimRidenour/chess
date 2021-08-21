import board


color = ('BLACK', 'WHITE')

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

    def get_moves(self):
        moves = []
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

class Queen:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

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

class Rook:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class Pawn:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
