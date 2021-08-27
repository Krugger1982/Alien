import pygame

class Ship():
    """ Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его стартовую позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение координаты центра нашего корабля
        self.x = float(self.rect.x)

        # флаг перемещения
        self.moving_right = False
        self.moving_left = False


    def update(self):
        # обновляет позицию с учетом флага
        # Обновляется не rect.x а сама переменная х
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # обновление атрибута rect на основани х
        self.rect.x = self.x
        
    def blitme(self):
        """Рисуем текущее место корабля"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ В начале каждой игры свой корабль устанавливается в центре нижней части экрана"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
