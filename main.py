import graphics
import pygame
import pieces
from board import Board as bd
from actions import action

player = pieces.Player(0, 0, graphics.PLAYER)

white_king = pieces.King(pieces.color[1], 4, 7, graphics.WHITE_KING)
white_queen = pieces.Queen(pieces.color[1], 3, 7, graphics.WHITE_QUEEN)
white_bishop1 = pieces.Bishop(pieces.color[1], 5, 7, graphics.WHITE_BISHOP)
white_bishop2 = pieces.Bishop(pieces.color[1], 2, 7, graphics.WHITE_BISHOP)
white_knight1 = pieces.Knight(pieces.color[1], 6, 7, graphics.WHITE_KNIGHT)
white_knight2 = pieces.Knight(pieces.color[1], 1, 7, graphics.WHITE_KNIGHT)
white_rook1 = pieces.Rook(pieces.color[1], 7, 7, graphics.WHITE_ROOK)
white_rook2 = pieces.Rook(pieces.color[1], 0, 7, graphics.WHITE_ROOK)

black_king = pieces.King(pieces.color[0], 4, 0, graphics.BLACK_KING)
black_queen = pieces.Queen(pieces.color[0], 3, 0, graphics.BLACK_QUEEN)
black_bishop1 = pieces.Bishop(pieces.color[0], 5, 0, graphics.BLACK_BISHOP)
black_bishop2 = pieces.Bishop(pieces.color[0], 2, 0, graphics.BLACK_BISHOP)
black_knight1 = pieces.Knight(pieces.color[0], 6, 0, graphics.BLACK_KNIGHT)
black_knight2 = pieces.Knight(pieces.color[0], 1, 0, graphics.BLACK_KNIGHT)
black_rook1 = pieces.Rook(pieces.color[0], 7, 0, graphics.BLACK_ROOK)
black_rook2 = pieces.Rook(pieces.color[0], 0, 0, graphics.BLACK_ROOK)

bd.add_piece(white_king)
bd.add_piece(white_queen)
bd.add_piece(white_bishop1)
bd.add_piece(white_bishop2)
bd.add_piece(white_knight1)
bd.add_piece(white_knight2)
bd.add_piece(white_rook1)
bd.add_piece(white_rook2)
bd.add_piece(black_king)
bd.add_piece(black_queen)
bd.add_piece(black_bishop1)
bd.add_piece(black_bishop2)
bd.add_piece(black_knight1)
bd.add_piece(black_knight2)
bd.add_piece(black_rook1)
bd.add_piece(black_rook2)
bd.add_player(player)

def main():
    key_up = True
    run = True
    FPS = 60
    clock = pygame.time.Clock()

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
        if keys[pygame.K_SPACE] and key_up:
            action(player)
            key_up = False
        if event.type == pygame.KEYUP:
            key_up = True

main()