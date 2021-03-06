import pygame
import os


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    mapFile.close()
    return level_map


def load_image(name, colorkey=None):
    fullname = os.path.join('data/img', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Map:
    def __init__(self, inf, color_word):

        self.image = inf[0]
        self.txt = inf[2]
        self.music = inf[1]
        self.score = inf[3]
        self.focus = inf[4]
        self.color_word = color_word

    def play(self, screen):

        map_on_play = load_level(self.txt)
        map_on_play = [map_on_play[i].split() for i in range(len(map_on_play))]
        screen.blit(pygame.image.load(self.image), [0, 0])

        color_counter = (3, 192, 60)
        paused = False
        game_lose = False
        post_game = False
        circles = []
        panel = pygame.sprite.Group()
        count = 0
        combo = 0
        max_combo = 0
        points = 0
        max_points = 0
        hp = 100
        accuracy = 100
        total_points = 0
        tap_inf_list = []
        music_end = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(music_end)
        list_reduce = []

        font_mark = pygame.font.Font(None, 1100)
        font1 = pygame.font.Font(None, 100)
        font2 = pygame.font.Font(None, 50)
        font3 = pygame.font.Font(None, 60)
        font_pause = pygame.font.Font(None, 150)
        text_pause1 = font_pause.render('Возобновить', 1, self.color_word)
        text_pause2 = font_pause.render('Заново', 1, self.color_word)
        text_pause3 = font_pause.render('Меню', 1, self.color_word)
        text_post1 = font3.render('Заново', 1, self.color_word)
        text_post2 = font3.render('Меню', 1, self.color_word)
        text_lose = font_pause.render('Ты проиграл', 1, self.color_word)

        game_over_sound = pygame.mixer.Sound('data/sound/game_over.wav')
        clear_map_sound = pygame.mixer.Sound('data/sound/applause.wav')
        button_sound = pygame.mixer.Sound('data/sound/button.wav')

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
                        if not paused:
                            paused = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if not paused and not post_game and not game_lose:
                        try:
                            panel.sprites()[0].update(event.pos, tap_inf_list, list_reduce[0])
                        except IndexError:
                            pass
                        if tap_inf_list != []:
                            del list_reduce[0]

                    if paused:
                        if not game_lose:
                            if 440 < x < 1140 and 100 < y < 300:
                                button_sound.play()
                                paused = False
                                pygame.mixer.music.unpause()
                        if 440 < x < 1140:
                            if 400 < y < 600:
                                button_sound.play()
                                return ['game', None]
                            elif 700 < y < 900:
                                button_sound.play()
                                return ['main', self.focus]
                    if post_game:
                        if 1320 < x < 1620:
                            if 800 < y < 900:
                                button_sound.play()
                                return ['game', None]
                            elif 950 < y < 1050:
                                button_sound.play()
                                return ['main', self.focus]

                if event.type == music_end:
                    post_game = True
                    clear_map_sound.play()
                    total_points = (accuracy * points) // max_combo
                    text_post3 = font1.render('Combo: X' + str(max_combo), 1, self.color_word)
                    text_post4 = font1.render('Points: ' + str(points), 1, self.color_word)
                    text_post5 = font1.render('Accuracy: ' + str(accuracy) + '%', 1, self.color_word)
                    text_post6 = font1.render('Total points: ' + str(total_points), 1, self.color_word)
                    f = open(self.score, 'a')
                    print(total_points, file=f)
                    f.close()
                    if accuracy > 95:
                        text_mark = font_mark.render('S', 1, (192, 192, 192))
                    elif 95 > accuracy > 90:
                        text_mark = font_mark.render('A', 1, (34, 139, 34))
                    elif 90 > accuracy > 85:
                        text_mark = font_mark.render('B', 1, (65, 105, 225))
                    elif 85 > accuracy > 80:
                        text_mark = font_mark.render('C', 1, (210, 105, 30))
                    elif 80 > accuracy:
                        text_mark = font_mark.render('D', 1, (255, 69, 0))

            if post_game:
                screen.blit(pygame.image.load(self.image), [0, 0])
                draw_pause([[1320, 800, 300, 100], [1320, 950, 300, 100], [50, 200, 900, 600]]
                           , screen)
                screen.blit(text_post1, (1400, 825))
                screen.blit(text_post2, (1400, 980))
                screen.blit(text_post3, (60, 250))
                screen.blit(text_post4, (60, 380))
                screen.blit(text_post5, (60, 510))
                screen.blit(text_post6, (60, 640))
                screen.blit(text_mark, (1230, 50))
                pygame.display.flip()

            elif paused:
                pygame.mixer.music.pause()
                screen.blit(pygame.image.load(self.image), [0, 0])
                if not game_lose:
                    draw_pause([[440, 100, 700, 200], [440, 400, 700, 200], [440, 700, 700, 200]], screen)
                    screen.blit(text_pause1, (445, 150))
                else:
                    screen.blit(text_lose, (445, 200))
                    draw_pause([[440, 400, 700, 200], [440, 700, 700, 200]], screen)
                screen.blit(text_pause2, (445, 450))
                screen.blit(text_pause3, (445, 750))
                pygame.display.flip()

            else:
                text1 = font1.render('X' + str(combo), 1, color_counter)
                text2 = font2.render(str(points), 1, color_counter)
                text3 = font2.render(str(accuracy) + '%', 1, color_counter)
                text4 = font2.render(str(hp), 1, color_counter)
                screen.blit(pygame.image.load(self.image), [0, 0])
                heart_group.draw(screen)
                screen.blit(text1, (0, 1020))
                screen.blit(text2, (1780, 0))
                screen.blit(text3, (1780, 50))
                screen.blit(text4, (35, 0))

                if count > len(panel.sprites()):
                    count -= 1
                    del circles[0]
                    if tap_inf_list == []:
                        break
                    if tap_inf_list[0][0] == 0:
                        combo = 0
                    else:
                        combo += tap_inf_list[0][0]
                    if combo > max_combo:
                        max_combo = combo
                    if hp + tap_inf_list[0][3] > 100:
                        hp = 100
                    elif hp + tap_inf_list[0][3] <= 0:
                        game_over_sound.play()
                        hp = 0
                        paused = True
                        game_lose = True
                    else:
                        hp += tap_inf_list[0][3]
                    points += tap_inf_list[0][1]
                    max_points += tap_inf_list[0][2]
                    accuracy = int(points / max_points * 100)
                    tap_inf_list = []

                position, flag = check_draw(position)
                if flag:
                    for i in map_on_play:
                        if position == float(i[0]):
                            draw_circle(int(i[2]), int(i[3]), i[1], panel, circles)
                            list_reduce.append(1)
                            count += 1
                for i in range(len(list_reduce)):
                    try:
                        panel.sprites()[i].update(None, tap_inf_list, list_reduce[i])
                    except IndexError:
                        pass
                for i in range(len(list_reduce)):
                    list_reduce[i] += 2
                draw_on(circles, panel, screen)
            pygame.display.flip()
            clock.tick(40)


def draw_on(group1, group2, screen):
    group2.draw(screen)
    for i in group1:
        pygame.draw.circle(screen, pygame.Color(i[2]), (i[0] + 50, i[1] + 50), 50)


class Stroke_panel(pygame.sprite.Sprite):
    def __init__(self, x, y, color, sprites):
        super().__init__(sprites)
        self.color = color
        self.x = x
        self.y = y
        self.image = pygame.Surface((270, 270), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (130, 130), 130, 1)
        self.rect = pygame.Rect(x - 80, y - 80, 500, 500)

    def update(self, args, list, reduce):
        self.image = pygame.Surface((270 - reduce * 2, 270 - reduce * 2), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(self.color), (130 - reduce, 130 - reduce),
                           130 - reduce, 1)
        self.rect = pygame.Rect(self.x - 80 + reduce, self.y - 80 + reduce, 500, 500)
        if reduce > 81:
            self.kill()
            tap_inf(0, list)
        elif args is not None:
            if self.rect.collidepoint(args):
                self.kill()
                if 81 > reduce > 70:
                    tap_inf(1, list)
                elif 70 > reduce > 30:
                    tap_inf(2, list)
                else:
                    tap_inf(3, list)


def check_draw(position):
    timing = pygame.mixer.music.get_pos() // 1000 / 10
    if timing == position:
        return position, False
    else:
        return timing, True


def draw_circle(x, y, color, panel, circles):
    Stroke_panel(x, y, color, panel)
    circles.append([x, y, color])


def tap_inf(inf, list):
    if inf == 0:
        list.append([0, 0, 300, -100])
    elif inf == 1:
        list.append([1, 300, 300, 20])
    elif inf == 2:
        list.append([1, 150, 300, -10])
    elif inf == 3:
        list.append([0, 50, 300, -20])


def draw_pause(coor_inf, screen):
    for i in coor_inf:
        pygame.draw.rect(screen, (239, 48, 56), i)
        pygame.draw.rect(screen, (255, 255, 255), i, 5)
