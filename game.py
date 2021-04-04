"""Module for initialize process"""

from models import Enemy, Player
from exceptions import GameOver, EnemyDown
import settings


def play():
    """Initialize game process"""

    name = str(input('Say your name: '))
    command = 0
    while command not in settings.GAME_COMMANDS:
        command = str(input('Введите start для начала игры: ').lower())
        if command == 'help':
            print('Help - список команд \nStart - старт игры \nShow scores - таблица результатов'
                  ' \nExit - выход из игры ')
            command = 0
        elif command == 'show scores':
            with open('scores.txt') as file:
                scores = [x.strip('\n') for x in file]
                for line in scores:
                    print(f"Place {line}")
            command = 0
        elif command == 'exit':
            raise SystemExit('You exit from game')
        if command == 'start':
            continue

    level = 1
    player = Player(name)
    enemy = Enemy(level=level)
    while 13 < 666:
        try:
            player.attack(enemy)
            player.defense(enemy)
            print(f" its enemy lives {enemy.lives}")
            print(f'its players lives {player.lives}')
        except EnemyDown:
            level += 1
            print(f"Level Up!\nLevel is set to {level}")
            player.score += 5
            enemy = Enemy(level=level)


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('The game is over')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye')
