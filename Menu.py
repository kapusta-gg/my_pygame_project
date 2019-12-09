import pygame


class Menu:
    def __init__(self, screen, maps):
        self.screen = screen
        self.maps = maps

    def render(self, what_in_focus, width, height):
        for i in self.maps:
            self.screen.blit(pygame.image.load(i[3]), [0, 0])
            pygame.draw.rect(self.screen, (32, 21, 94), [width - 600, height // 2.4, 600, 200])
            pygame.draw.rect(self.screen, (255, 255, 255), [width - 600, height // 2.4, 600, 200], 4)
            pygame.draw.circle(self.screen, (32, 21, 94), [width - 600, int(height // 2.4) + 100], 100)

            font = pygame.font.Font(None, 100)
            text = font.render(i[2], 1, (255, 255, 255))
            self.screen.blit(text, [width - 580, height // 2 - 40])

            font = pygame.font.Font(None, 40)
            text = font.render(i[1], 1, (255, 255, 255))
            self.screen.blit(text, [width - 540, height // 2 + 40])

    def what_play(self, what_in_focus):
        for i in self.maps:
            return [i[3], i[4], i[5]]