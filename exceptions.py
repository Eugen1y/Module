"""Module for exceptions """


class GameOver(Exception):
    '''
    Ending of a game with write score in file if score in top 10
    '''

    def __init__(self, name, score):
        self.name = name
        self.score = score

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


class EnemyDown(Exception):
    """Exception if enemy lives is 0"""


class SystemExit(Exception):
    """Exit game"""
