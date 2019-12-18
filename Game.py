import pygame
import sqlite3
import sys
from win32api import GetSystemMetrics
from Menu import Menu
from Map import Map

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

what_visible = 'menu'
int_map_focus = 0
con = sqlite3.connect("data/collections.db")
cur = con.cursor()
v = 30
fps = 60
time = 0

def play_music(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    map_focus = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    map_focus += 1
                if event.button == 4:
                    map_focus -= 1
                if event.button == (1 or 2):
                    map_play = menu.what_play(map_focus)
                    return map_play

            screen.fill((0, 0, 0))
            if map_focus < 0:
                map_focus = 0
            elif map_focus > 1:
                map_focus -= 1
            map = cur.execute("SELECT * FROM collection WHERE map_on_list=" + str(map_focus)).fetchall()
            menu = Menu(screen, map)
            menu.render(map_focus, width, height)
        pygame.display.flip()


map_play = start_screen()
print(map_play)
map = Map(map_play)
map.play(screen)
running = True

pygame.quit()

