import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

import pygame

class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """ Инициирует иргу и создает игровые ресурсы """
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)        # 
        self.settings.screen_width = self.screen.get_rect().width                # задаем ширину экрана
        self.settings.screen_height = self.screen.get_rect().height             # задаем высоту экрана
        pygame.display.set_caption("Alien Invasion")                        # надпись вверху экрана

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
                                    # отслеживаем клавиатуру и мышь
            self.ship.update()
                                    # отслеживаем изменения позиции корабля
            self._update_bullets()
                                    # И позиции всех снарядов            
            self._update_screen()
                                    # обновление экрана с каждым проходом цикла
            self._update_aliens()
                                    # Обновление пришельцев

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Обновление позиции снарядов и уничтожение старых снарядов"""

        # Позиции снарядов
        self.bullets.update()
        
        # Удаление старых снарядов
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        # Действия по проверке коллизий (совпадения координат корабля пришельцев и снаряда)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Проверка попадания в пришельцев
        # при попадании и снаряд и пришелец удаляются
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # метод groupcollide() разбирается с коллизиями.
        # Он проверяет наличие коллизий между снарядами и вражескими кораблями,
        # и удаляет обоих участников коллизии

        # При уничтожении всех кораблей противника создаем новый флот
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

        
                
    def _update_aliens(self):
        """ Обновляет позиции всех чужих в их флоте"""
        self._check_fleet_edges()
        self.aliens.update()


    def _update_screen(self):
        """ Обновляет изображения на экране и отобразжает новый экран """
        self.screen.fill(self.settings.bg_color)
        # при каждом проходе цикла прорисовывается экран
        self.ship.blitme()
        # и отображается корабль
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Обновляем позиции всех сгруппированных снарядов
        self.aliens.draw(self.screen)
        # И позицию вражеского корабля 

        
        # Отображение последнего прорисованнoго экрана
        pygame.display.flip()

    def _create_alien(self, alien_number, row_number):
        """ Создание очередного прищшельца и размещение его в очередном ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)          # Добавляем его в группу пришельцев

    def _create_fleet(self):
        """ Создаем флот пришельцеы"""   
        
        # Создание одного абстрактного пришельца. 
        # Он нужен для расчетов ширины, чтоб не обращаться все время к атрибуту rect         
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size             # Извлекаем размерения одного корабля для расчетов
        # Посчитаем сколько их уместится в ряду
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # ... и подсчитаем сколько мы можем уместить рядов на экране
        ship_height = self.ship.rect.height
        # ОСтавим место для своего корабля  - его высоту плюс троекратную высоту вражеского корабля
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

        # определяем количество рядов
        number_rows = available_space_y // (2 * alien_height)

        # Создадим флот ряд за рядом
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """ Проверяет весь флот, не уперся ли кто-нибудь в край экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Весь флот опускается немного вниз и начинает двигаться в другую сторону """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



        
if __name__ == '__main__':
    # Создание экземпляра игры
    ai = AlienInvasion()
    ai.run_game()
