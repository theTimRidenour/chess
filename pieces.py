color = ('BLACK', 'WHITE')

class King:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window, x, y):
        window.blit(self.img, (x, y))

    def get_moves():
        return {'forward': [(1, 0)], 'forward-right': [(1, 1)], 'right': [(0, 1)], 'backward-right': [(-1, 1)], 'backward': [(-1, 0)], 'backward-left': [(-1, -1)], 'left': [(0, -1)], 'forward-left': [(1, -1)]}

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


class Bishop:
    def __init__(self, color, x, y, img):
        self.color = color
        self.x = x
        self.y = y
        self.img = img
        self.has_moved = False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

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
