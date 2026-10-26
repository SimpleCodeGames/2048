# Raw Board + Spawn Tile

import pygame
import sys
import random

CYAN = (0, 255, 255)
GRAY = (96, 96, 96)

# Number of Tile
tile = 4

# Board Size
board_y = 4
board_x = 4
board = []

for y in range(board_y):
    board.append([0] * board_x)

# 100 = size of tile
# 25 = size of gap between tile
# 150 = score board
tab_y = tile * 100 + tile * 25 + 150
tab_x = tile * 100 + tile * 25 + 25

def make_board():
    spawn_y = random.randint(0, 3)
    spawn_x = random.randint(0, 3)

    board[spawn_y][spawn_x] = 1

def main():
    pygame.init()
    pygame.display.set_caption("2048 - 001")
    screen = pygame.display.set_mode((475, 475))
    clock = pygame.time.Clock()

    make_board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_board()
        for y in range(board_y):
            for x in range(board_x):
                length = 100
                X = x * (length + 25)
                Y = y * (length + 25)

                if board[y][x] == 0: # Board
                    pygame.draw.rect(screen, CYAN, [X, Y, length, length])

                if board[y][x] == 1: # Tile
                    pygame.draw.rect(screen, GRAY, [X, Y, length, length])
        
        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    main()