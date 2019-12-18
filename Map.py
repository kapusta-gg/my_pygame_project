import pygame
from mutagen.mp3 import MP3
from win32api import GetSystemMetrics


class Map:
    def __init__(self, inf):

        self.image = inf[0]
        self.db = inf[2]
        self.music = inf[1]

    def play(self, screen):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(1)
            screen.blit(pygame.image.load(self.image), [0, 0])
            pygame.display.flip()
