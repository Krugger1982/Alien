import pygame.font


class Button():

    def __init__(self, ai_game, msg):
        """ Инициализирует атрибуты кнопки """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначим размеры и свойства кнопки
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание ее по центру
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение в виде кнопки появляется только один раз
        self.prep_msg(msg)


    def prep_msg(self, msg):
        """ Преобразует сообщение msg в прямоугольник с текстом,
            текст выравнен по центру прямоугольника"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # Здесь msg - текст сообщения, которое появится в кнопке
        # Второй аргумент - признак сглаженного текста
        # self.text_color - задаем цвет букв
        # self.button_color задаем цвет фона, в нашем случае он совпадет с цветом самой кнопки.
        #                                       по умолчанию - будет прозрачный фон

        self.msg_image_rect = self.msg_image.get_rect()
        # задаем размеры текстового прямоугольника
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Отображение пустой кнопки и вывод собщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
