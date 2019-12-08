import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.maps = [['Christopher Larkin', 'hornet', 'Files_of_map/map_img.png'],
                     ['Christopher Larkin', 'hornet', 'Files_of_map/image.png']]

    def render(self, what_in_focus, width, height):
        for i in self.maps:
            if self.maps.index(i) == what_in_focus:
                self.screen.blit(pygame.image.load(i[2]), [0, 0])
                pygame.draw.rect(self.screen, (76, 88, 102), [width - 600, height // 2.4, 600, 200])
