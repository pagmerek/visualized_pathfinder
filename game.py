import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

screen.fill((192, 192, 192))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
