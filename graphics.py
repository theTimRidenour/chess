import pygame
import os
from pygame.constants import HIDDEN

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

BG = pygame.image.load(os.path.join('assets', 'board.png'))
PLAYER = pygame.image.load(os.path.join('assets', 'player.png'))
SAFE_SQUARE = pygame.image.load(os.path.join('assets', 'safe_square.png'))
ATTACK_SQARE = pygame.image.load(os.path.join('assets', 'attack_square.png'))
ROOK_SQUARE = pygame.image.load(os.path.join('assets', 'rook_square.png'))

#Pieces
BLACK_KING = pygame.image.load(os.path.join('assets', 'black-king.png'))
BLACK_QUEEN = pygame.image.load(os.path.join('assets', 'black-queen.png'))
BLACK_BISHOP = pygame.image.load(os.path.join('assets', 'black-bishop.png'))
BLACK_KNIGHT = pygame.image.load(os.path.join('assets', 'black-knight.png'))
BLACK_PAWN = pygame.image.load(os.path.join('assets', 'black-pawn.png'))
BLACK_ROOK = pygame.image.load(os.path.join('assets', 'black-rook.png'))
WHITE_KING = pygame.image.load(os.path.join('assets', 'white-king.png'))
WHITE_QUEEN = pygame.image.load(os.path.join('assets', 'white-queen.png'))
WHITE_BISHOP = pygame.image.load(os.path.join('assets', 'white-bishop.png'))
WHITE_KNIGHT = pygame.image.load(os.path.join('assets', 'white-knight.png'))
WHITE_PAWN = pygame.image.load(os.path.join('assets', 'white-pawn.png'))
WHITE_ROOK = pygame.image.load(os.path.join('assets', 'white-rook.png'))
