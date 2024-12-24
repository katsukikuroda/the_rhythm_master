import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600
JUST_TIMING_y = 550

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

circle_y = 0

running = True
while running:
    screen.fill(0)

    pygame.draw.circle(screen, (255, 0, 0), (350, JUST_TIMING_y), 25)

    pygame.draw.circle(screen, (0, 255, 0), (350, circle_y), 25)
    circle_y += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                y_difference = abs(circle_y - JUST_TIMING_y)
                if y_difference < 12:
                    print("good")
                elif y_difference < 24:
                    print("ok")
                elif y_difference < 40:
                    print("bad")

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()