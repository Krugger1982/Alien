import sys

import pygame

class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """ Инициирует иргу и создает игровые ресурсы """
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Alien Invasion")
        # Назначим цвет фона
        self.bg_color = (230, 200, 230)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            # отслеживаем клавиатуру и мышь
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # при каждом прохоже цикла прорисовывается экран
            self.screen.fill(self.bg_color)
            # Отображение послежнего прорисованнго экрана
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра игры
    ai = AlienInvasion()
    ai.run_game()
