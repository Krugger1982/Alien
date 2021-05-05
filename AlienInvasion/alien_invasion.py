import sys
from settings import Settings

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



    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # отслеживаем клавиатуру и мышь
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # при каждом прохоже цикла прорисовывается экран
            self.screen.fill(self.settings.bg_color)
            # Отображение послежнего прорисованнго экрана
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра игры
    ai = AlienInvasion()
    ai.run_game()
