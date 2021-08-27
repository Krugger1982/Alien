class GameStats():
    """ Отслеживание статистических данных"""

    def __init__(self, ai_game):
        """ Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """ Обнуляет статистику которая меняется в ходе игры. Это происходит в начале каждой игры """
        self.ships_left = self.settings.ship_limit
        # Это количество жизней
