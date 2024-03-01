# 2048 Python game project by Nikul

import pygame
import random

# The above two packages are used. Pygame package is used for game creation and the random package is used for generating random numbers.


WIDTH = 400
HEIGHT = 500
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048 Game by Nikul')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

#This block of code is used to set up the game window of a certain height and width, a caption for the game window and creating a clock which controls the framerate and lastly establishing the frames per second.

# 2048 game color library
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

# The above block of code defines the colours of the game for the background, the tiles and the text.

# Game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''
score = 0
high_score = 0

#This block of code defines the variables for the game.
# board_values = game board values
# game_over = game_over status
# spawn_new = the number of initial tiles spawned
# direction = direction of movement
# score = current score during gameplay
# high_score = highest score from multiple gameplays


def draw_over():
    pygame.draw.rect(screen, 'black', [50, 50, 300, 100], 0, 10)
    game_over_text1 = font.render('Game Over!', True, 'white')
    game_over_text2 = font.render('Press Enter to Restart', True, 'white')
    screen.blit(game_over_text1, (130, 65))
    screen.blit(game_over_text2, (70, 105))

def render_scores():
    score_text = font.render(f'Score: {score}', True, 'black')
    high_score_text = font.render(f'High Score: {high_score}', True, 'black')
    screen.blit(score_text, (10, 410))
    screen.blit(high_score_text, (10, 450))


def take_turn(direc, board):
    global score
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direc == 'UP':
        for j in range(4):
            for i in range(1, 4):
                if board[i][j] != 0:
                    temp_i = i
                    while temp_i > 0 and board[temp_i - 1][j] == 0:
                        board[temp_i - 1][j] = board[temp_i][j]
                        board[temp_i][j] = 0
                        temp_i -= 1
                    if temp_i > 0 and board[temp_i - 1][j] == board[temp_i][j] and not merged[temp_i - 1][j]:
                        board[temp_i - 1][j] *= 2
                        score += board[temp_i - 1][j]
                        board[temp_i][j] = 0
                        merged[temp_i - 1][j] = True

    elif direc == 'DOWN':
        for j in range(4):
            for i in range(2, -1, -1):
                if board[i][j] != 0:
                    temp_i = i
                    while temp_i < 3 and board[temp_i + 1][j] == 0:
                        board[temp_i + 1][j] = board[temp_i][j]
                        board[temp_i][j] = 0
                        temp_i += 1
                    if temp_i < 3 and board[temp_i + 1][j] == board[temp_i][j] and not merged[temp_i + 1][j]:
                        board[temp_i + 1][j] *= 2
                        score += board[temp_i + 1][j]
                        board[temp_i][j] = 0
                        merged[temp_i + 1][j] = True

    elif direc == 'LEFT':
        for i in range(4):
            for j in range(1, 4):
                if board[i][j] != 0:
                    temp_j = j
                    while temp_j > 0 and board[i][temp_j - 1] == 0:
                        board[i][temp_j - 1] = board[i][temp_j]
                        board[i][temp_j] = 0
                        temp_j -= 1
                    if temp_j > 0 and board[i][temp_j - 1] == board[i][temp_j] and not merged[i][temp_j - 1]:
                        board[i][temp_j - 1] *= 2
                        score += board[i][temp_j - 1]
                        board[i][temp_j] = 0
                        merged[i][temp_j - 1] = True

    elif direc == 'RIGHT':
        for i in range(4):
            for j in range(2, -1, -1):
                if board[i][j] != 0:
                    temp_j = j
                    while temp_j < 3 and board[i][temp_j + 1] == 0:
                        board[i][temp_j + 1] = board[i][temp_j]
                        board[i][temp_j] = 0
                        temp_j += 1
                    if temp_j < 3 and board[i][temp_j + 1] == board[i][temp_j] and not merged[i][temp_j + 1]:
                        board[i][temp_j + 1] *= 2
                        score += board[i][temp_j + 1]
                        board[i][temp_j] = 0
                        merged[i][temp_j + 1] = True

    return board

def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if board[row][col] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        full = True
    return board, full

def draw_board():
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)
    render_scores()


def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)

# The next large chunk of code consists of different functions which are useful for defining the main aspects of the game.
# draw_over() = Initiates the gameover message and creates a prompt to restart the game
# render_scores() = displays the current high_score and score on the screen
# take_turn(direc, board) = initiates the movement for tiles in specific directions either left, right, up, or down
# new_pieces(board) = randomly spawns new tiles on the game board
# draw_board() = creates the game board background
# draw_pieces(board) = creates the tiles present on the game board

run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_values)
    if spawn_new or init_count < 2:
        board_values, game_over = new_pieces(board_values)
        spawn_new = False
        init_count += 1
    if direction != '':
        temp_board = [row[:] for row in board_values]
        board_values = take_turn(direction, board_values)
        if board_values != temp_board:
            board_values, _ = new_pieces(board_values)
        direction = ''
    if game_over:
        draw_over()
        if score > high_score:
            high_score = score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = 'UP'
            elif event.key == pygame.K_DOWN:
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            if event.key == pygame.K_r:  
                if score > high_score:  
                    high_score = score
                board_values = [[0 for _ in range(4)] for _ in range(4)]
                spawn_new = True
                init_count = 0
                score = 0
                direction = ''
                game_over = False
    pygame.display.flip()

pygame.quit()

# The main game loop while run: above is responsible for the overall flow of the game ensuring that the screen is updated and refreshing or restarting the game when necessary. 
# Lastly the event loop (direction) is responsible for controlling the direction of tile movement using key presses up, down, left or right arrow keys and using the letter r to restart the game. 
# This concludes my project on the 2048 game.



