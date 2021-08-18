import pygame
import os
from pygame.constants import HIDDEN

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

BG = pygame.image.load(os.path.join('assets', 'board.png'))

#Pieces
BLACK_KING = pygame.image.load(os.path.join('assets', 'black-king.png'))
WHITE_KING = pygame.image.load(os.path.join('assets', 'white-king.png'))
