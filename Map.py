import pygame
from mutagen.mp3 import MP3
from win32api import GetSystemMetrics


class Map:
    def __init__(self, inf):
        self.image = inf[0]
        self.musicLenght = MP3(inf[1]).info.length
        self.db = inf[2]
        self.music = inf[1]

    def play(self, screen, time):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

        running = True
        while running:
            print(pygame.mixer.music.get_pos() // 1000)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(1)
                if int(pygame.mixer.music.get_pos() // 1000) == 4:
                    pygame.draw.circle(screen, ((0, 0, 0)), [60, 250], 40)
            screen.blit(pygame.image.load(self.image), [0, 0])
            pygame.display.flip()
