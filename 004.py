# Score System Added

import pygame
import sys
import random

colors = [(46, 26, 71), (94, 58, 141), (123, 82, 171), (156, 107, 201), (184, 133, 228), (200, 156, 243), (215, 179, 255), (226, 196, 255), (238, 213, 255), (248, 230, 255), (253, 238, 255), (255, 245, 255)]

# Number of Tile
tile = 4

# Tile Size
length = 100
gap = 10

# Board Size
board_y = 4
board_x = 4
board = []
done = []

# Top Space
top = 50

for y in range(board_y):
    board.append([0] * board_x)
    done.append([0] * board_x)

def make_done():
    for y in range(board_y):
        for x in range(board_x):
            done[y][x] = 0

# 100 = size of tile
# 10 = size of gap between tile
tab_y = tile * length + tile * gap + gap
tab_x = tile * length + tile * gap + gap

def make_board():
    spawn_y = random.randint(0, 3)
    spawn_x = random.randint(0, 3)

    board[spawn_y][spawn_x] = 1

def spawn():
    empty = [(y, x) for y in range(board_y) for x in range(board_x) if board[y][x] == 0]
    if empty: 
        y, x = random.choice(empty)
        board[y][x] = random.randint(1, 2)

def shift_up(score):
    for x in range(board_x):
        for y in range(1, board_y):
            if board[y][x] == 0:
                continue
            i = y
            while i >= 1:
                if board[i - 1][x] == 0:
                    board[i - 1][x] = board[i][x]
                    board[i][x] = 0
                    done[i - 1][x] = done[i][x]
                    done[i][x] = 0
                    i -= 1
                elif (done[i][x] == 0) and (done[i - 1][x] == 0) and (board[i - 1][x] == board[i][x]):
                    board[i - 1][x] += 1
                    score += 2**board[i - 1][x]
                    board[i][x] = 0
                    done[i][x] = 0
                    done[i - 1][x] = 1
                    break
                else:
                    break
    return score

def shift_down(score):
    for x in range(board_x):
        for y in range(board_y - 2, -1, -1):
            if board[y][x] == 0:
                continue
            i = y
            while i <= board_y - 2:
                if board[i + 1][x] == 0:
                    board[i + 1][x] = board[i][x]
                    board[i][x] = 0
                    done[i + 1][x] = done[i][x]
                    done[i][x] = 0
                    i += 1
                elif (done[i][x] == 0) and (done[i + 1][x] == 0) and (board[i + 1][x] == board[i][x]):
                    board[i + 1][x] += 1
                    score += 2**board[i + 1][x]
                    board[i][x] = 0
                    done[i][x] = 0
                    done[i + 1][x] = 1
                    break
                else:
                    break
    return score

def shift_left(score):
    for y in range(board_y):
        for x in range(1, board_x):
            if board[y][x] == 0:
                continue
            i = x
            while i >= 1:
                if board[y][i - 1] == 0:
                    board[y][i - 1] = board[y][i] 
                    board[y][i] = 0
                    done[y][i - 1] = done[y][i]
                    done[y][i] = 0
                    i -= 1
                elif (done[y][i] == 0) and (done[y][i - 1] == 0) and (board[y][i - 1] == board[y][i]):
                    board[y][i - 1] += 1
                    score += 2**board[y][i - 1]
                    board[y][i] = 0
                    done[y][i] = 0
                    done[y][i - 1] = 1
                    break
                else:
                    break
    return score

def shift_right(score):
    for y in range(board_y):
        for x in range(board_x - 2, -1, -1):
            if board[y][x] == 0:
                continue
            i = x
            while i <= board_x - 2:
                if board[y][i + 1] == 0:
                    board[y][i + 1] = board[y][i]
                    board[y][i] = 0
                    done[y][i + 1] = done[y][i]
                    done[y][i] = 0
                    i += 1
                elif (done[y][i] == 0) and (done[y][i + 1] == 0) and (board[y][i + 1] == board[y][i]):
                    board[y][i + 1] += 1
                    score += 2**board[y][i + 1]
                    board[y][i] = 0
                    done[y][i] = 0
                    done[y][i + 1] = 1
                    break
                else:
                    break
    return score

def is_game_over():
    if any(0 in row for row in board): 
        return False
    for y in range(4):
        for x in range(4):
            if x < 3 and board[y][x] == board[y][x + 1]: return False
            if y < 3 and board[y][x] == board[y + 1][x]: return False
    return True

def main():
    pygame.init()
    pygame.display.set_caption("2048 - 004")
    screen = pygame.display.set_mode((tab_x, tab_y + top))
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 50)
    make_board()
    game_over = False

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for y in range(board_y):
                        for x in range(board_x):
                            board[y][x] = 0
                    make_board()
                    score = 0
                    game_over = False

                if not game_over:
                    if event.key == pygame.K_UP:
                        score = shift_up(score)
                    if event.key == pygame.K_DOWN:
                        score = shift_down(score)
                    if event.key == pygame.K_LEFT:
                        score = shift_left(score)
                    if event.key == pygame.K_RIGHT:
                        score = shift_right(score)
                
                    spawn()
                    print(done)
                    print(board)
                    make_done()
                
                    if is_game_over():
                        game_over = True

        screen.fill((0, 0, 0))

        text_surface = font.render(f"{score}", True, (255, 255, 255))
        screen.blit(text_surface, (top/10, top/5))

        for y in range(board_y):
            for x in range(board_x):
                X = x * (length + gap) + gap
                Y = y * (length + gap) + gap + top

                pygame.draw.rect(screen, colors[board[y][x]], [X, Y, length, length], border_radius = 5)
                if board[y][x] != 0:
                    text_surface = font.render(f"{2**board[y][x]}", True, (0, 0, 0))
                else:
                    text_surface = font.render("", True, colors[7 - board[y][x]])
                screen.blit(text_surface, (X, Y))

        if game_over:
            clock.tick(100)

            gray_overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA); gray_overlay.fill((128, 128, 128, 150))
            screen.blit(gray_overlay, (0, 0))

            msg = font.render(f"{score}", True, (255, 0, 0))
            screen.blit(msg, ((tile * (length + 10) + 10)/2, top/2))
            
            msg = font.render("Try Again!", True, (255, 0, 0))
            pygame.draw.rect(screen, colors[0], [150, 185, 175, 45], border_radius = 5)
            screen.blit(msg, (155, 190))

        pygame.display.update()
        clock.tick(25)

if __name__ == '__main__':
    main()