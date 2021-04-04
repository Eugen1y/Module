"""Module for exceptions """


class GameOver(Exception):
    '''
    Ending of a game with write score in file if score in top 10
    '''

    def __init__(self, name, score):
        self.name = name
        self.score = score
        print('name :', self.name, 'Scores : ', self.score)



class EnemyDown(Exception):
    """Exception if enemy lives is 0"""


class SystemExit(Exception):
    """Exit game"""
