import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """ Этот класс представляет корабль пришельцев """

    def __init__(self, ai_game):
        """ Инициирует одного пришельца в его начальной позиции """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загружаем изображение с примоугольником rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в ЛВУ
        self.rect.x = self.rect.width           # Интервал по высоте от края экрана равен размеру самого пришельца
        self.rect.y = self.rect.height          # ... и  по ширине

        # Сохранение горизонтальной позиции пришельца
        self.x = float(self.rect.x) 

    def check_edges(self):
        """ Возвращает True если какой-нибудь из кораблей пришельцев "уперся" в край экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """ Перемещает пришельцев вправо """
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
