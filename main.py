import graphics
import pygame
import pieces
from board import Board as bd
from actions import action, check_for_check, check_for_checkmate

# create player and add to player board
player = pieces.Player(0, 0, graphics.PLAYER)
bd.add_player(player)

# create all the pieces and place on board
pieces.load_pieces(graphics)

def main():
    key_up = True
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    # draw and display graphics every 1/FPS seconds
    def redraw_window():
        graphics.WIN.blit(graphics.BG, (0, 0))
        bd.draw_pieces(graphics.WIN)
        bd.draw_safe_squares(graphics.WIN, graphics.SAFE_SQUARE)
        bd.draw_attack_squares(graphics.WIN, graphics.ATTACK_SQARE)
        bd.draw_player(graphics.WIN, player)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        # if player presses X on corner of screen close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # players moves
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
        if keys[pygame.K_SPACE] and key_up:
            action(player)
            key_up = False
        if event.type == pygame.KEYUP:
            key_up = True

if __name__ == '__main__':
    main()