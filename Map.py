import pygame
from mutagen.mp3 import MP3
from win32api import GetSystemMetrics


class Map:
    def __init__(self, inf):
        self.image = inf[0]
        self.musicLenght = MP3(inf[1]).info.length
        self.db = inf[2]

    def draw(self, screen, time):
        screen.blit(pygame.image.load(self.image), [0, 0])
        if time == 4:
            pygame.draw.circle(screen, (255, 255, 255), [60, 250], 40)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(1)
            screen.fill((0, 0, 0))
