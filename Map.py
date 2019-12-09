import pygame
from mutagen.mp3 import MP3
from win32api import GetSystemMetrics


class Map:
    def __init__(self, inf):
        self.image = inf[0]
        self.musicLenght = MP3(inf[1]).info.length
        self.db = inf[2]

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), [60, 250], 40)
