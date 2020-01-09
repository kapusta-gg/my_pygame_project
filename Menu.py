import pygame


class Menu:
    def __init__(self, screen, maps):
        self.screen = screen
        self.maps = maps

    def render(self, width, height):
        list_scores = []
        for i in self.maps:
            f = open(i[6], 'r')
            for j in f:
                if j != ' ':
                    j = j.split('\n')
                    list_scores.append(int(j[0]))
            list_scores.sort(reverse=True)
            self.screen.blit(pygame.image.load(i[3]), [0, 0])
            pygame.draw.rect(self.screen, (239, 48, 56), [50, 150, 400, 800])
            pygame.draw.rect(self.screen, (255, 255, 255), [50, 150, 400, 800], 5)
            pygame.draw.rect(self.screen, (239, 48, 56), [width - 600, height // 2.4, 600, 200])
            pygame.draw.rect(self.screen, (255, 255, 255), [width - 600, height // 2.4, 600, 200], 4)
            pygame.draw.circle(self.screen, (239, 48, 56), [width - 600, int(height // 2.4) + 100], 100)

            font1 = pygame.font.Font(None, 100)
            text = font1.render(i[1], 1, (255, 146, 24))
            self.screen.blit(text, [width - 580, height // 2 - 40])

            font2 = pygame.font.Font(None, 40)
            text = font2.render(i[2], 1, (255, 146, 24))
            self.screen.blit(text, [width - 540, height // 2 + 40])

            font3 = pygame.font.Font(None, 60)
            text1 = font3.render('Топ набранных очков', 1, (255, 146, 24))
            text2 = font3.render('на карте', 1, (255, 146, 24))
            self.screen.blit(text1, [50, 40])
            self.screen.blit(text2, [150, 80])

            y_draw = 150
            count = 0
            for j in list_scores:
                text = font1.render(str(j), 1, (255, 146, 24))
                pygame.draw.rect(self.screen, (255, 255, 255), [50, y_draw, 400, 200], 5)
                self.screen.blit(text, [80, y_draw + 60])
                y_draw += 200
                count += 1
                if count == 4:
                    break

    def what_play(self):
        for i in self.maps:
            return [i[3], i[4], i[5], i[6], i[0]]