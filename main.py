import pygame
from pygame.locals import *
# lesson2 効果音を鳴らす で追加
from pygame import mixer
#
# lesson3 曲の管理 で追加
import data
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

# lesson2 タイミングの判定 で変更 lesson3 複数の円に対してキーの判定を適用する で circle_y = 0を削除
#

# lesson2 時間と画面表示のズレをなくす で追加 lesson3でfps = 100削除
frame_count = 1
start_time = pygame.time.get_ticks()
#

# lesson3 曲の管理 で追加
selected_music = 0
#

# lesson3 譜面を作成して複数の円を表示させる で追加
A = "A"
N = None
note_count = 0
notes = []
GREEN = (0, 255, 0)
#

# lesson3 譜面を作成して複数の円を表示させる で追加
last_spawn_time = start_time
#

# lesson3 譜面を作成して複数の円を表示させる で追加
class Note:
    def __init__(self, x, y, sound, color, speed):
        self.x = x
        self.y = y
        self.sound = sound
        self.speed = speed
        self.size = 25
        self.color = color
        self.flag = False

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
#

running = True
while running:
    screen.fill(0)
    # lesson3 複数の円に対してキーの判定を適用する で追加
    key_a_flag = False
    #

    # lesson2 タイミングの判定 で追加&変更 lesson3 譜面を作成して複数の円を表示させる で動円削除
    pygame.draw.circle(screen, (255, 0, 0), (350, JUST_TIMING_y), 25)
    #

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                # lesson2 タイミングの判定 で変更&追加 lesson3 複数の円に対してキーの判定を適用する で キー判定を削除
                #
                # lesson2 効果音を鳴らす で追加
                sound_se_1.play()
                #
                # lesson3 複数の円に対してキーの判定を適用する で追加
                key_a_flag = True
                #

        if event.type == pygame.QUIT:
            running = False

    # lesson3 譜面を作成して複数の円を表示させる で追加  複数の円に対してキーの判定を適用する でfor文変更
    if pygame.time.get_ticks() - last_spawn_time >= 60000 / data.music_list[selected_music]["bpm"] / 2:
        if note_count < len(data.music_list[selected_music]["score"]):
            if data.music_list[selected_music]["score"][note_count] == A:
                notes.append( Note(350, 0, A, GREEN, 3) )
            elif data.music_list[selected_music]["score"][note_count] == N:
                pass
            last_spawn_time = pygame.time.get_ticks()
            note_count += 1

    if key_a_flag:
        for note in notes[:]:
            note.update()
            note.draw(screen)
            if note.y > HEIGHT:
                notes.remove(note)

            y_difference = abs(note.y - JUST_TIMING_y)
            if y_difference < 12:
                print("good")
                notes.remove(note)
            elif y_difference < 20:
                print("ok")
                notes.remove(note)
            elif y_difference < 40:
                print("bad")
                notes.remove(note)

    else:
        for note in notes[:]:
            note.update()
            note.draw(screen)
            if note.y > HEIGHT:
                notes.remove(note)
    #

    # lesson2 時間と画面表示のズレをなくす で追加　lesson3でfps部分を変更
    while (pygame.time.get_ticks() - start_time) < (1000 / data.music_list[selected_music]["fps"] * frame_count):
        pass
    frame_count += 1
    # 

    pygame.display.flip()