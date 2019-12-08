import pygame
from win32api import GetSystemMetrics
from Menu import Menu

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
what_visible = 'menu'
map__in_focus = 0
maps = [['Christopher Larkin', 'Hornet', 'Files_of_map/map_img.png', 'Files_of_map/map_music.mp3'],
        ['zxczxc', 'ZXCzxccZXcSDcds', 'Files_of_map/image.png', 'Files_of_map/map_music.mp3']]


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
        if what_visible == 'menu':
            screen.fill((0, 0, 0))
            b = Menu(screen, maps)
            if map__in_focus < 0:
                map__in_focus = 0
            elif map__in_focus > len(maps) - 1:
                map__in_focus = len(maps) - 1
            a = b.render(map__in_focus, width, height)
        else:
            pass
        pygame.display.flip()

pygame.quit()
