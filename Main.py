import pygame
from win32api import GetSystemMetrics

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
backround_pos = [0, 0]
backround_img = pygame.image.load('map.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        screen.blit(backround_img, backround_pos)
        pygame.display.flip()

pygame.quit()