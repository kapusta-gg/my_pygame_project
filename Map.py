import pygame
import os


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    return level_map


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Map:
    def __init__(self, inf):

        self.image = inf[0]
        self.txt = inf[2]
        self.music = inf[1]

    def play(self, screen):
        map_on_play = load_level(self.txt)
        map_on_play = [map_on_play[i].split() for i in range(len(map_on_play))]

        circles = []
        panel = pygame.sprite.Group()
        count = 0
        combo = 0
        points = 0
        max_points = 0
        hp = 100
        accuracy = 100
        tap_inf_list = []

        font1 = pygame.font.Font(None, 100)
        font2 = pygame.font.Font(None, 50)

        sprite = pygame.sprite.Sprite()
        heart_group = pygame.sprite.Group()
        sprite.image = load_image('heart.png')
        sprite.rect = sprite.image.get_rect()
        heart_group.add(sprite)

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
                    panel.update(event.pos, tap_inf_list)

            text1 = font1.render('X' + str(combo), 1, (3, 192, 60))
            text2 = font2.render(str(points), 1, (3, 192, 60))
            text3 = font2.render(str(accuracy) + '%', 1, (3, 192, 60))
            text4 = font2.render(str(hp), 1, (3, 192, 60))

            screen.blit(pygame.image.load(self.image), [0, 0])
            heart_group.draw(screen)
            screen.blit(text1, (0, 1020))
            screen.blit(text2, (1780, 0))
            screen.blit(text3, (1780, 50))
            screen.blit(text4, (35, 0))

            draw_on(circles, panel, screen)
            position, flag = check_draw(position)
            if flag:
                for i in map_on_play:
                    if position == float(i[0]):
                        draw_circle(int(i[2]), int(i[3]), i[1], panel, circles)
                        count += 1
            panel.update(None, tap_inf_list)
            if count > len(panel):
                count -= 1
                del circles[0]
                if tap_inf_list == 0:
                    combo = 0
                else:
                    combo += tap_inf_list[0][0]
                if hp + tap_inf_list[0][3] > 100:
                    hp = 100
                elif hp + tap_inf_list[0][3] < 0:
                    hp = 0
                else:
                    hp += tap_inf_list[0][3]
                points += tap_inf_list[0][1]
                max_points += tap_inf_list[0][2]
                accuracy = int(points / max_points * 100)
                tap_inf_list = []
            clock.tick(60)
            pygame.display.flip()


def draw_on(group1, group2, screen):
    group2.draw(screen)
    for i in group1:
        pygame.draw.circle(screen, pygame.Color(i[2]), (i[0] + 50, i[1] + 50), 50)


class Stroke_panel(pygame.sprite.Sprite):
    def __init__(self, x, y, color, sprites):
        super().__init__(sprites)
        self.reduce = 1
        self.color = color
        self.image = pygame.Surface((6 * 50, 6 * 50), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (130, 130), 130, 1)
        self.rect = pygame.Rect(x - 80, y - 80, 500, 500)

    def update(self, args, list):
        self.image.fill(pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.Color(self.color), (130, 130),
                           130 - self.reduce, 1)
        self.reduce += 2
        if self.reduce > 81:
            self.kill()
            tap_inf(0, list)
        elif args is not None:
            if self.rect.collidepoint(args):
                self.kill()
                if 81 > self.reduce > 70:
                    tap_inf(1, list)
                elif 70 > self.reduce > 30:
                    tap_inf(2, list)
                else:
                    tap_inf(3, list)


def check_draw(position):
    timing = int(pygame.mixer.music.get_pos() / 1000) / 10
    if timing == position:
        return position, False
    else:
        return timing, True


def draw_circle(x, y, color, panel, circles):
    Stroke_panel(x, y, color, panel)
    circles.append([x, y, color])


def tap_inf(inf, list):
    if inf == 0:
        list.append([0, 0, 300, -20])
    elif inf == 1:
        list.append([1, 300, 300, 20])
    elif inf == 2:
        list.append([1, 150, 300, -10])
    else:
        list.append([0, 0, 300, -20])


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image