import pygame


grid_width, grid_height = 10, 20
tileSize = 45
Game_res = grid_width * tileSize, grid_height * tileSize
fps = 60

grid = [pygame.Rect(x * tileSize, y * tileSize, tileSize, tileSize) for x in range(grid_width) for y in range(grid_height)]

block_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
               [(0, -1), (-1, -1), (-1, 0), (0, 0)],
               [(-1, 0), (-1, 1), (0, 0), (0, -1)],
               [(0, 0), (-1, 0), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, -1)],
               [(0, 0), (0, -1), (0, 1), (1, -1)],
               [(0, 0), (0, -1), (0, 1), (-1, 0)]]

block_rect = pygame.Rect(0, 0, tileSize - 2, tileSize - 2)
field = [[0 for i in range(grid_width)] for j in range(grid_height)]

pygame.init()

screen = pygame.display.set_mode(Game_res)
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

while True:
    screen.fill(pygame.Color('dark blue'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        [pygame.draw.rect(screen, (40, 40, 40), i_rect, 1) for i_rect in grid]

    pygame.display.flip()
    clock.tick(fps)