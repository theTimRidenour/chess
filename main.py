import graphics
import pygame
import pieces
from board import Board as bd
from actions import action

player = pieces.Player(0, 0, graphics.PLAYER)

white_king = pieces.King(pieces.color[1], 4, 7, graphics.WHITE_KING)

black_king = pieces.King(pieces.color[0], 4, 0, graphics.BLACK_KING)

bd.add_piece(white_king)
bd.add_piece(black_king)
bd.add_player(player)

def main():
    key_up = True
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        graphics.WIN.blit(graphics.BG, (0, 0))
        bd.draw_pieces(graphics.WIN)
        bd.draw_player(graphics.WIN, player)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and player.get_y() != 7 and key_up:
            bd.move_player(player, player.get_x(), player.get_y() + 1)
            key_up = False
        if keys[pygame.K_UP] and player.get_y() != 0 and key_up:
            bd.move_player(player, player.get_x(), player.get_y() - 1)
            key_up = False
        if keys[pygame.K_LEFT] and player.get_x() != 0 and key_up:
            bd.move_player(player, player.get_x() - 1, player.get_y())
            key_up = False
        if keys[pygame.K_RIGHT] and player.get_x() != 7 and key_up:
            bd.move_player(player, player.get_x() + 1, player.get_y())
            key_up = False
        if keys[pygame.K_a]:
            action(player)
            key_up = False
        if event.type == pygame.KEYUP:
            key_up = True

main()