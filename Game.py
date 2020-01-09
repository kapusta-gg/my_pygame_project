import pygame
import sqlite3
import sys
from win32api import GetSystemMetrics
from Menu import Menu
from Map import Map

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

sound = pygame.mixer.Sound('data/button.wav')

int_map_focus = 0
con = sqlite3.connect("data/collections.db")
cur = con.cursor()
v = 30
fps = 60
time = 0
what_visible = 'main'
start_flag = True
font = pygame.font.Font(None, 120)
text = font.render('opu!', 1, (255, 146, 24))
map_focus = 0


def play_music(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


def terminate():
    pygame.quit()
    sys.exit()


def main_screen(map_focus):
    global start_flag
    if start_flag:
        play_music('data/circles.mp3')
    else:
        pygame.mixer.music.stop()
    while True:
        count_map = cur.execute("SELECT map_on_list FROM collection WHERE map_on_list!='' ").fetchall()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if start_flag:
                        terminate()
                    else:
                        play_music('data/circles.mp3')
                        start_flag = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if not start_flag:
                    if event.button == 5:
                        map_focus += 1
                    if event.button == 4:
                        map_focus -= 1
                    if 0 > map_focus or map_focus > len(count_map) - 1:
                        pass
                    else:
                        sound.play()
                    if event.button == (1 or 2):
                        map_focus = menu.what_play()
                        return [map_focus, 'game']
                elif start_flag:
                    if event.button == (1 or 2):
                        if 480 < y < 625:
                            if 850 < x < 1000:
                                sound.play()
                                start_flag = False
                                pygame.mixer.music.stop()
                            elif 1055 < x < 1205:
                                terminate()

            if start_flag:
                screen.blit(pygame.image.load('data/start_img.jpg'), [0, 0])
                pygame.draw.rect(screen, [239, 48, 56], [0, 480, 1980, 145])
                pygame.draw.circle(screen,  (239, 48, 56), [600, 550], 200)
                screen.blit(text, [530, 500])
                pygame.draw.circle(screen, (255, 255, 255), [600, 550], 200, 15)
                screen.blit(pygame.image.load('data/play.png'), [850, 480])
                screen.blit(pygame.image.load('data/exit.png'), [1070, 490])
                pygame.draw.polygon(screen, (255, 0, 255), [[850, 480], [1050, 480], [1000, 625], [800, 625]], 5)
                pygame.draw.polygon(screen, (0, 255, 127), [[1005, 625], [1055, 480], [1255, 480], [1205, 625]], 5)
            elif not start_flag:
                if map_focus < 0:
                    map_focus = 0
                elif map_focus > len(count_map) - 1:
                    map_focus -= 1
                map = cur.execute("SELECT * FROM collection WHERE map_on_list=" + str(map_focus)).fetchall()
                menu = Menu(screen, map)
                menu.render(width, height)
        pygame.display.flip()

running = True
while running:
    if what_visible == 'main':
        map_play = main_screen(map_focus)
        what_visible = map_play[1]
    elif what_visible == 'game':
        map = Map(map_play[0])
        play = map.play(screen)
        what_visible = play[0]
        map_focus = play[1]