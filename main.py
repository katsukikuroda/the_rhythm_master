import pygame
from pygame.locals import *
# lesson2 効果音を鳴らす で追加
from pygame import mixer
#

WIDTH = 800
HEIGHT = 600
JUST_TIMING_y = 550

pygame.init()
# lesson2 効果音を鳴らす で追加
mixer.init()
#
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# lesson2 効果音を鳴らす で追加
sound_se_1 = mixer.Sound('sounds/se_1.mp3')
sound_se_1.set_volume(1)
#

# lesson2 タイミングの判定 で変更
circle_y = 0
#

# lesson2 時間と画面表示のズレをなくす で追加
fps = 100
frame_count = 1
start_time = pygame.time.get_ticks()
#

running = True
while running:
    screen.fill(0)

    # lesson2 タイミングの判定 で追加&変更
    pygame.draw.circle(screen, (255, 0, 0), (350, JUST_TIMING_y), 25)

    pygame.draw.circle(screen, (0, 255, 0), (350, circle_y), 25)
    #
    circle_y += 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                # lesson2 タイミングの判定 で変更&追加
                y_difference = abs(circle_y - JUST_TIMING_y)
                if y_difference < 12:
                    print("good")
                elif y_difference < 24:
                    print("ok")
                elif y_difference < 40:
                    print("bad")
                #
                # lesson2 効果音を鳴らす で追加
                sound_se_1.play()
                #


        if event.type == pygame.QUIT:
            running = False

    # lesson2 時間と画面表示のズレをなくす で追加
    while (pygame.time.get_ticks() - start_time) < (1000 / fps * frame_count):
        pass
    frame_count += 1
    # 

    pygame.display.flip()