# circleアニメーションのおまけ
import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

c_x = 0
c_y = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    screen.fill(0)

    pygame.draw.circle(screen, (0, 255, 0), (c_x, c_y), 25)
    if c_x < WIDTH and c_y < HEIGHT:
        c_x += 1
        c_y += 1
    else:
        c_x = 0
        c_y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()