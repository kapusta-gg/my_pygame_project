import pygame
from win32api import GetSystemMetrics
from Menu import Menu

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
back_pos = [0, 0]
back_img = pygame.image.load('Files_of_map/map_img.png')
what_visible = 'menu'
map__in_focus = 0


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
            if event.button == 5:
                map__in_focus += 1
            if event.button == 4:
                map__in_focus -= 1
        if what_visible == 'menu':
            screen.fill((0, 0, 0))
            b = Menu(screen)
            b.render(map__in_focus, width, height)
        else:
            screen.blit(back_img, back_pos)
        pygame.display.flip()

pygame.quit()
