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

    def update(self):
        """ Перемезает пришельцев вправо """
        self.x += self.settings.alien_speed
        self.rect.x = self.x
