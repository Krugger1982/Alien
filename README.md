# Alien


Это небольшая компьютерная игра, написанная на Python с использованием Pygame для десктопных компьютеров.
Она напоминает некогда популярную на 8-битных приставках игру Galaxian.

## Процесс игры
Игрок управляет лазерной пушкой, передвигая её горизонтально, в нижней части экрана, а также отстреливая инопланетян, надвигающихся сверху экрана.
Целью игры является уничтожение трех рядов по десять инопланетян, которые двигаются горизонтально, а также вертикально, по направлению к низу экрана.
Игрок имеет бесконечное количество патронов.
Попадая в инопланетянина, игрок уничтожает его, за что получает очки.
При уничтожении инопланетян (с прохождением уровня) увеличивается скорость движения врагов.
При уничтожении всех инопланетян появляется новая, ещё более сильная волна. 
Количество новых волн инопланетян неограниченно, что делает игру бесконечной.

## Управление игрой.
В начале игры нажмите (клик мышкой) кнопку "Play"
Перемещение своего корабля - кнопки "влево" и "вправо"
Стрельба - кнопкой "пробел"
Выход из игры - кнопка Q.

## Установка

Для того чтоб установить игру на локальную машину клонируйте репозиторий  
```
git clone https://github.com/Krugger1982/alien/
```

### Запуск

Для запуска игры в необходимо установить модуль pygame 
1. Установите и активируйте виртуальное окружение.  
Cоздание виртуального окружения:  
```
$ python3 -m venv venv
```

Активация виртуального окружения:  
```$ source venv/bin/activate``` (команда для Linux/MacOS)  
или:  
```$ source venv/Scripts/activate``` (команда для Windows)  
при активированном виртуальном окружении установите зависимости из файла requirements.txt
выполните команду:  
```$ pip install pygame ```

В папке с файлом alien_invasion.py выполните команду запуска игры:  
```$ python3 alien_invasion.py ```  

Или откройте сам файл и запустите его на выполнение.

Автор:
Алексей
