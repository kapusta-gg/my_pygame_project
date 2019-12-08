import pygame
from win32api import GetSystemMetrics

pygame.init()

size = width, height = GetSystemMetrics(0), GetSystemMetrics(1)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0, 255, 255))
        pygame.display.flip()

pygame.quit()