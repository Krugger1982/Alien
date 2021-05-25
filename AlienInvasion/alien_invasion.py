import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

import pygame

class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """ Инициирует иргу и создает игровые ресурсы """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            # отслеживаем клавиатуру и мышь
            self.ship.update()
            # отслеживаем изменения позиции корабля
            self.bullets.update()
            # И позиции всех снарядов

            #Удаление снарядов, долеевших до верхнего края
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            
            self._update_screen()
            # обновление экрана с каждым проходом цикла
            

    def _check_events(self):
        # отслеживаем клавиатуру и мышь
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # реакция на нажатие клавиш
        if event.key == pygame.K_RIGHT:
            # переместить корабль вправо
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # переместить корабль влево
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup_events(self, event):
        # реакция на отпускание клавиш
        if event.key == pygame.K_RIGHT:
            # конец перемещения корабля вправо
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # конец перемещения корабля влево
            self.ship.moving_left = False

    def fire_bullet(self):
        """ Выстрел - создаем снаряд и включаем его в р-группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """ Обновляет изображения на экране и отобразжает новый экран """
        self.screen.fill(self.settings.bg_color)
        # при каждом проходе цикла прорисовывается экран
        self.ship.blitme()
        # и отображается корабль
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Обновляем позиции всех сгруппированных снарядов

        
        # Отображение последнего прорисованнoго экрана
        pygame.display.flip()


        
if __name__ == '__main__':
    # Создание экземпляра игры
    ai = AlienInvasion()
    ai.run_game()
