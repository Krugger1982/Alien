class Settings():
    """ Класс для хранения настроек игры
    """

    def __init__(self):
        """ Инициализирует настройки игры
        """
        # Параметры экрана
        self.screen_width = 1300
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # параметры нашего корабля
        self.ship_limit = 1

        # параметры пули
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 9

        # Параметры чужих кораблей        
        self.fleet_drop_speed = 50
        # self.fleet_drop_speed - это величина, на которую "шагает" вражеский флот дойдя до края экрана
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости врагов (с каждым уровнем каждый подбитый враг приносит больше очков
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 0.3

        self.fleet_direction = 1
        # fleet_direction - это флаг направления движения кораблей. 1 - вправо, -1 - влево

        # Начальная "стоимость" одного подбитого врага
        self.alien_points = 50



    def increase_speed(self):
        """ увеличивает настройки скорости и стоимость пришельцев """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
