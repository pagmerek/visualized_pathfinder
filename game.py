import pygame
from grid import path_grid
pygame.init()

screen = pygame.display.set_mode((527, 527))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255,182,193)

screen.fill(BLACK)

width=15
height=15
margin=1

running = True
all_rects = []
for y in range(15, 497, width+margin):
    row = []
    for x in range(15, 497, height+margin):
        rect = path_grid(pygame.Rect(x, y, width, height), "basic")
        row.append([rect, WHITE])
    all_rects.append(row)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
            # check which rect was clicked and change its color on list
        for row in all_rects:
            for item in row:
                rect, color = item
                if rect.collidepoint(pygame.mouse.get_pos()):
                    item[1] = RED

        screen.fill(BLACK)

    for row in all_rects:
        for item in row:
            rect, color = item
            path_grid.path_rect.pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
