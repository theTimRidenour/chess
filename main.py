import graphics
import pygame
import pieces
from board import Board as bd

white_king = pieces.King(pieces.color[1], 4, 7, graphics.WHITE_KING)

black_king = pieces.King(pieces.color[0], 4, 0, graphics.BLACK_KING)

bd.add_piece(white_king)
bd.add_piece(black_king)

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        graphics.WIN.blit(graphics.BG, (0, 0))
        bd.draw_pieces(graphics.WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and black_king.get_y() != 7:
            bd.move_piece(black_king, black_king.get_x(), black_king.get_y() + 1)
        if keys[pygame.K_UP] and black_king.get_y() != 0:
            bd.move_piece(black_king, black_king.get_x(), black_king.get_y() - 1)
        if keys[pygame.K_LEFT] and black_king.get_x() != 0:
            bd.move_piece(black_king, black_king.get_x() - 1, black_king.get_y())
        if keys[pygame.K_RIGHT] and black_king.get_x() != 7:
            bd.move_piece(black_king, black_king.get_x() + 1, black_king.get_y())

main()