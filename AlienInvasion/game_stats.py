class GameStats():
    """ Отслеживание статистических данных"""

    def __init__(self, ai_game):
        """ Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Флаг, показывающий активное состояние игры
        self.game_active = False

        # Рекордный счет - он не сбрасывается
        self.high_score = 0

    def reset_stats(self):
        """ Обнуляет статистику которая меняется в ходе игры. Это происходит в начале каждой игры """
        self.ships_left = self.settings.ship_limit
        # Это количество жизней

        self.score = 0
        # Инициализируем (обнуляем) счет в начале игры

        self.level = 1
        # инициализируем (обнуляем) счетчик уровня игры
