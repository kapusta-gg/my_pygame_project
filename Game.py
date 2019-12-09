import pygame, sqlite3
from win32api import GetSystemMetrics
from Menu import Menu

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
what_visible = 'menu'
map__in_focus = 0
con = sqlite3.connect("collections.db")
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
                    map__in_focus += 1
                if event.button == 4:
                    map__in_focus -= 1
                if event.button == (1 or 2):
                    inf_for_game = b.what_play(map__in_focus)
                    what_visible = 'game'
                    play_music(inf_for_game[1])

        if what_visible == 'menu':
            screen.fill((0, 0, 0))
            if map__in_focus < 0:
                map__in_focus = 0
            elif map__in_focus > 1:
                map__in_focus -= 1
            maps = cur.execute("SELECT * FROM collection WHERE map_on_list=" + str(map__in_focus)).fetchall()
            b = Menu(screen, maps)
            b.render(map__in_focus, width, height)
        elif what_visible == 'game':
            screen.blit(pygame.image.load(inf_for_game[0]), [0, 0])
        pygame.display.flip()

pygame.quit()
