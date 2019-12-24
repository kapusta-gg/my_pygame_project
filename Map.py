import pygame
from win32api import GetSystemMetrics


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


class Map:
    def __init__(self, inf):

        self.image = inf[0]
        self.txt = inf[2]
        self.music = inf[1]

    def play(self, screen):
        map_on_play = load_level(self.txt)
        map_on_play = [map_on_play[i].split() for i in range(len(map_on_play))]

        circles = pygame.sprite.Group()
        panel = pygame.sprite.Group()

        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
        position = -0.1

        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            screen.blit(pygame.image.load(self.image), [0, 0])
            sprite_draw(circles, panel, screen)
            timing = int(pygame.mixer.music.get_pos() / 1000) / 10
            position, flag = check_draw(position, timing)
            if flag:
                for i in map_on_play:
                    if position == float(i[0]):
                        draw_circle(int(i[2]), int(i[3]), i[1], panel, circles)
                        #Stroke_panel(int(i[2]), int(i[3]), i[1], panel)
                        #Ball(int(i[2]), int(i[3]), i[1], circles)
            circles.draw(screen)
            panel.update()
            clock.tick(60)
            pygame.display.flip()


def sprite_draw(group1, group2, screen):
    group1.draw(screen)
    group2.draw(screen)


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, color, sprites):
        super().__init__(sprites)
        self.image = pygame.Surface((2 * 50, 2 * 50), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (50, 50), 50)
        self.rect = pygame.Rect(x, y, 2 * 50, 2 * 50)


class Stroke_panel(pygame.sprite.Sprite):
    def __init__(self, x, y, color, sprites):
        super().__init__(sprites)
        self.reduce = 1
        self.color = color
        self.image = pygame.Surface((6 * 50, 6 * 50), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (130, 130), 130, 1)
        self.rect = pygame.Rect(x - 80, y - 80, 500, 500)

    def update(self):
        self.image = pygame.Surface((6 * 50, 6 * 50), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(self.color), (130, 130),
                           130 - self.reduce, 1)
        self.reduce += 2
        if self.reduce > 80:
            self.kill()


def check_draw(position, timing):
    timing = int(pygame.mixer.music.get_pos() / 1000) / 10
    if timing == position:
        return position, False
    else:
        return timing, True


def draw_circle(x, y, color, panel, circles):
    Stroke_panel(x, y, color, panel)
    Ball(x, y, color, circles)

