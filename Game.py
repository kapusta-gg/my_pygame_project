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
what_visible = 'menu'

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
                    sound.play()
                    map_focus += 1
                if event.button == 4:
                    sound.play()
                    map_focus -= 1
                if event.button == (1 or 2):
                    sound.play()
                    map_focus = menu.what_play()
                    return [map_focus, 'game']

            screen.fill((0, 0, 0))
            if map_focus < 0:
                map_focus = 0
            elif map_focus > 1:
                map_focus -= 1
            map = cur.execute("SELECT * FROM collection WHERE map_on_list=" + str(map_focus)).fetchall()
            menu = Menu(screen, map)
            menu.render(width, height)
        pygame.display.flip()

running = True
while running:
    if what_visible == 'menu':
        map_play = start_screen()
        what_visible = map_play[1]
    elif what_visible == 'game':
        map = Map(map_play[0])
        what_visible = map.play(screen)


terminate()

