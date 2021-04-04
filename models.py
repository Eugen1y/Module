import random
import settings
from exceptions import GameOver, EnemyDown


class Player:
    def __init__(self, name):
        self.lives = settings.LIVES
        self.name = name
        self.score = settings.SCORE

    def decrease_lives(self):
        self.lives = self.lives - 1
        if self.lives == 0:
            Score.save_scores(name=self.name, score=self.score)
            raise GameOver(name=self.name, score=self.score)


    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return settings.DRAW
        elif attack == 1 and defense == 2 or attack == 2 and defense == 3 \
                or attack == 3 and defense == 1:
            return settings.WIN
        else:
            return settings.LOSE

    def attack(self, enemy_obj):
        """Initialize attack"""
        attack1 = 0
        while attack1 not in settings.ALLOWED_ATTACK:
            try:
                attack1 = int(input("1 - WIZARD, 2 - WARRIOR, 3 - ROGUE.Выберите атаку:  "))
                if attack1 not in settings.ALLOWED_ATTACK:
                    raise ValueError
            except ValueError:
                print('Incorrect input')

        enemy_obj.attack = enemy_obj.select_attack()
        if self.fight(attack1, enemy_obj.attack) == 0:
            print("It's a draw!")
        if self.fight(attack1, enemy_obj.attack) == 1:
            enemy_obj.decrease_lives()
            self.score += 1
            print("You attacked successfully!")
        if self.fight(attack1, enemy_obj.attack) == -1:
            print("You missed!")

    def defense(self, enemy_obj):
        """Print result of defense """
        defense1 = 0
        while defense1 not in settings.ALLOWED_ATTACK:
            defense1 = int(input("1 - WIZARD, 2 - WARRIOR, 3 - ROGUE.Выберите защиту:  "))

        enemy_obj.attack = Enemy.select_attack()
        if self.fight(enemy_obj.attack, defense1) == 0:
            print("It's a draw!")
        if self.fight(enemy_obj.attack, defense1) == 1:
            self.decrease_lives()
            print("You fail enemy attack!")
        if self.fight(enemy_obj.attack, defense1) == -1:
            print("You blocked attack!")


class Enemy:
    """Create enemy"""

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """Select attack value from 1 to 3"""
        result = random.randint(1, 3)
        return result

    def decrease_lives(self):
        """Decrease lives by 1"""
        self.lives = self.lives - 1
        if self.lives == 0:
            raise EnemyDown
class Score:
    @staticmethod
    def save_scores(name, score):
        new_score = f"1 {name} {score}"
        with open('scores.txt') as file:
            scores = [x.strip('\n') for x in file]
            scores_array = [x.split(' ') for x in scores]
            scores_array.append(new_score.split(' '))
            scores_array = sorted(scores_array, key=lambda x: int(x[-1]), reverse=True)
            for score in range(len(scores_array)):
                scores_array[score][0] = str(score + 1)
                with open('scores.txt', 'w+') as file_sc:
                    for entry in scores_array:
                        if int(entry[0]) <= 10:
                            file_sc.write(' '.join(entry) + '\n')

