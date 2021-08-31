import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """ Класс для хранения и вывода цифровой инфомации"""

    def __init__(self, ai_game):
        """ Инициализирует атрибуты подсчета очков"""
        self.ai_game = ai_game        
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки щрифта для вывода счета
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # подготовка изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """ преобразует надпись с текстом, отображающую счет, в графическую катинку
        """
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Выводим очки счета в верхнем правом углу
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        # отступ от правой кромки экрана - 20 пикселей, выравнивание всегда будет по правому краю
        # таким образом при увеличении счета тступ будет сохраняться
        self.score_rect.top = 20
        # отступ сверху будет тоже равен 20 пикселей

    def show_score(self):
        """Выводим счет на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
    def prep_high_score(self):
        """ преобразует надпись о рекрдном счете в картинку"""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = 'Highscore = ' + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render( high_score_str, True, self.text_color, self.settings.bg_color)

        # Вывод рекордных очkов в верху экрана посередине
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """ проверяет, не появился ли новый рекорд """
        if self.stats.score > self.stats.high_score:            # Если кто-то побил рекорд
            self.stats.high_score = self.stats.score            # Новый рекорд заносим в память
            self.prep_high_score()

    def prep_level(self):
        """ Преобразуем уровень в графическое изображение"""
        level_str = 'Level  ' + str(self.stats.level)
        self.level_image = self.font.render(level_str, True,self.text_color, self.settings.bg_color)

        # Вывод уровня в верху экрана справа, под счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom + 20

    def prep_ships(self):
        """ Проверяет сколько кораблей ("жизней") осталось у игрока"""
        self.ships = Group()
        # Cоздаем группу кораблей (экземплр класса Group
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)           # Создаем объект корабля
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = 10
            # задаем их координаты: отступы слева и сверху по10 пикс, расположены в ряд в левом верхнем углу
            self.ships.add(ship)


            


        
