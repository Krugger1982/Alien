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
        self.ship_speed = 1.5

        # параметры пули
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 9

        # Параметры чужих кораблей
        self.alien_speed = 0.3
        self.ship_limit = 3
        self.fleet_drop_speed = 50
        # self.fleet_drop_speed - это величина, на которую "шагает" вражеский флот дойдя до края экрана 
        self.fleet_direction = 1
        # fleet_direction - это флаг направления движения кораблей. 1 - вправо, -1 - влево
        
        
