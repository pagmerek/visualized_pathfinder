import pygame
from grid import path_grid

pygame.init()

screen = pygame.display.set_mode((527, 527))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 182, 193)
BROWN = (218, 165, 32)

screen.fill(BLACK)

width = 15
height = 15
margin = 1

running = True
all_rects = []
counter = 0

for y in range(15, 497, width + margin):
    row = []
    for x in range(15, 497, height + margin):
        rect = path_grid(pygame.Rect(x, y, width, height), "basic")
        row.append([rect, WHITE])
    all_rects.append(row)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        for row in all_rects:
            for item in row:
                rect, color = item
                if rect.getRect().collidepoint(pygame.mouse.get_pos()):
                    if counter == 0 and not item[0].visited:
                        item[1] = BROWN
                        item[0].visited = True
                        item[0].kind = "start"
                        counter += 1
                    elif counter == 1 and not item[0].visited:
                        item[1] = BROWN
                        item[0].visited = True
                        item[0].kind = "end"
                        counter += 1
                    elif counter > 1 and not item[0].visited:
                        item[1] = BLACK
                        item[0].kind = "obstacle"

        screen.fill(BLACK)

    for row in all_rects:
        for item in row:
            rect, color = item
            pygame.draw.rect(screen, color, rect.getRect())
    pygame.display.flip()
