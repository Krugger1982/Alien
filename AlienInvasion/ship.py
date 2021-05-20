import pygame

class Ship():
    """ Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его стартовую позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False


    def update(self):
        # обновляет позицию с учетом флага
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
        
    def blitme(self):
        """Рисуем текущее место корабля"""
        self.screen.blit(self.image, self.rect)

    
