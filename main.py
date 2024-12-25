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

# lesson4 画面の作成 で追加
font_select = pygame.font.Font("ipaexg.ttf", 40)
#
# lesson4 スコア機能の追加 で追加 & さらに変更
font_game = pygame.font.Font("ipaexg.ttf", 50)
#
# lesson4 画面の作成 で追加
font_result = pygame.font.Font("ipaexg.ttf", 40)
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

# lesson4  で追加
note_flag = False
#

# lesson4  で追加
music_flag = False
#

# lesson4 スコア機能の追加 で追加
score = 0
#

# lesson4 画面の作成 で追加
SELECT_SCENE = 0
GAME_SCENE = 1
RESULT_SCENE = 2
scene = SELECT_SCENE
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

    # lesson4 画面の作成 で追加&変更
    if scene == SELECT_SCENE:
        select_text1 = font_select.render("Select Music", False, (255, 255, 255))
        select_text2 = font_select.render("Click Music", False, (255, 255, 255))
        screen.blit(select_text1, (80, 80))
        screen.blit(select_text2, (80, 120))

        for index, music in enumerate(data.music_list):
            music_text = font_select.render(f"{index + 1} : {music['title']}", False, (255, 255, 255))
            screen.blit(music_text, (80, 200 + 40 * index))

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                for index in range(len(data.music_list)):
                    if 80 < x < 720 and 200 + 40 * index < y < 240 + 40 * index:
                        selected_music = index
                        scene = GAME_SCENE
                        start_time = pygame.time.get_ticks()
                        last_spawn_time = pygame.time.get_ticks()
                        music_flag = False
                        note_flag = False
                        score = 0
                        note_count = 0
                        frame_count = 1

            if event.type == pygame.QUIT:
                running = False

    #


    # lesson4 画面の作成 で追加 (以下のコードにインデントの追加)
    elif scene == GAME_SCENE:
    #
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

        # lesson4 音楽の再生 で追加
        if pygame.time.get_ticks() - start_time >= data.music_list[selected_music]["delay"] and note_flag == False:
            note_flag = True
        #

        # lesson3 譜面を作成して複数の円を表示させる で追加  複数の円に対してキーの判定を適用する でfor文変更 lesson4 音楽の再生 で条件文 and note_flagの追加
        if pygame.time.get_ticks() - last_spawn_time >= 60000 / data.music_list[selected_music]["bpm"] / 2 and note_flag:
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
                    # lesson4 スコア機能の追加 で追加 
                    score += 100
                    #
                    notes.remove(note)
                elif y_difference < 20:
                    print("ok")
                    # lesson4 スコア機能の追加 で追加 
                    score += 50
                    #
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

        # lesson4 音楽の再生 で追加
        if pygame.time.get_ticks() - start_time >= 3000 and music_flag == False:
            mixer.music.load(data.music_list[selected_music]["music"])
            mixer.music.set_volume(0.5)
            mixer.music.play()
            music_flag = True
        #

        # lesson4 スコア機能の追加 で追加
        text = font_game.render(f"スコア: {score}", False, (255,255,255))
        screen.blit(text, [20, 100])    
        #

        # lesson4 画面の作成 で追加
        if pygame.time.get_ticks() - start_time > data.music_list[selected_music]["time"] + 6000:
            scene = RESULT_SCENE
            pygame.mixer.music.stop()
        #

        # lesson2 時間と画面表示のズレをなくす で追加　lesson3でfps部分を変更
        while (pygame.time.get_ticks() - start_time) < (1000 / data.music_list[selected_music]["fps"] * frame_count):
            pass
        frame_count += 1
        # 

    # lesson4 画面の作成 で追加&変更
    elif scene == RESULT_SCENE:
        score_text = font_result.render(f"Score : {score}", False, (255, 255, 255))
        retry_text = font_result.render("if you retry, press 'R' key", False, (255, 255, 255))
        screen.blit(score_text, (200, 120))
        screen.blit(retry_text, (200, 360))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    scene = SELECT_SCENE

            if event.type == pygame.QUIT:
                running = False
    #

    pygame.display.flip()