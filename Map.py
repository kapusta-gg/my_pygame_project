import pygame
from win32api import GetSystemMetrics


class Map:
    def __init__(self, inf):

        self.image = inf[0]
        self.txt = inf[2]
        self.music = inf[1]

    def play(self, screen):
        map_on_play = self.load_level(self.txt)
        map_on_play = [map_on_play[i].split() for i in range(len(map_on_play))]

        all_sprites = pygame.sprite.Group()

        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()

        previous = 0.0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            if int(pygame.mixer.music.get_pos() / 1000) / 10 == 0.1:
                pass

            screen.blit(pygame.image.load(self.image), [0, 0])
            for i in map_on_play:
                timing = int(pygame.mixer.music.get_pos() / 1000) / 10
                if timing == float(i[0]):
                    Stroke_panel(50, int(i[2]), int(i[3]), i[1], all_sprites)
                    Ball(50, int(i[2]), int(i[3]), i[1], all_sprites)
            all_sprites.draw(screen)
            pygame.display.flip()

    def load_level(self, filename):
        filename = filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
        return level_map


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, color, sprites):
        super().__init__(sprites)
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)


class Stroke_panel(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, color, sprites):
        super().__init__(sprites)
        self.image = pygame.Surface(( 30 * radius, 30 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (radius + 60, radius + 60), radius + 60, 5)
        self.rect = pygame.Rect(x - 60, y - 60, 10 * radius, 10 * radius)
