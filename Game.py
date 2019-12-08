import pygame
from win32api import GetSystemMetrics
from Menu import Menu

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
backround_pos = [0, 0]
backround_img = pygame.image.load('Files_of_map/map_img.png')


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
        play_music('Files_of_map/map_music.mp3')
        screen.blit(backround_img, backround_pos)
        pygame.display.flip()

pygame.quit()
