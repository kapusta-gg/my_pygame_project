import pygame, sqlite3
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

def play_music(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if what_visible == 'menu':
                if event.button == 5:
                    int_map_focus += 1
                if event.button == 4:
                    int_map_focus -= 1
                if event.button == (1 or 2):
                    inf_for_game = menu.what_play(int_map_focus)
                    what_visible = 'game'
                    play_music(inf_for_game[1])

        if what_visible == 'menu':
            screen.fill((0, 0, 0))
            if int_map_focus < 0:
                map__in_focus = 0
            elif int_map_focus > 1:
                int_map_focus -= 1
            map_focus = cur.execute("SELECT * FROM collection WHERE map_on_list=" + str(int_map_focus)).fetchall()
            menu = Menu(screen, map_focus)
            menu.render(int_map_focus, width, height)
        elif what_visible == 'game':
            screen.blit(pygame.image.load(inf_for_game[0]), [0, 0])
            map = Map(inf_for_game)
            map.draw(screen)
        pygame.display.flip()

pygame.quit()
