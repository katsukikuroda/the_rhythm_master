import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_y = 100

running = True
while running:
    screen.fill(0)

    pygame.draw.circle(screen, (0, 255, 0), (100, circle_y), 25)
    circle_y += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                print("key down")

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()