import sys
from settings import Settings
from ship import Ship

import pygame

class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """ Инициирует иргу и создает игровые ресурсы """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            # отслеживаем клавиатуру и мышь

            self._update_screen()
            # обновление экрана с каждым проходом цикла
            

    def _check_events(self):
        # отслеживаем клавиатуру и мышь
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        

    def _update_screen(self):
        """ Обновляет изображения на экране и отобразжает новый экран """
        self.screen.fill(self.settings.bg_color)
        # при каждом проходе цикла прорисовывается экран
        self.ship.blitme()
        # и отображается корабль
        
        # Отображение послежнего прорисованнго экрана
        pygame.display.flip()
        
if __name__ == '__main__':
    # Создание экземпляра игры
    ai = AlienInvasion()
    ai.run_game()
