from __future__ import print_function
from axelrod import Player
import random

class AllDefector(Player):
    name = 'All Defector'

    @staticmethod
    def strategy(opponent):
        return 'D'


class PlayerGreen1(Player):
    name = 'Player Green 1'

    @staticmethod
    def strategy(opponent):
        return 'D' if opponent.cooperations < opponent.defections else 'C'

class PlayerGreen2(Player):
    name = 'Player Green 2'

    def strategy(self, opponent):
        if len(opponent.history) == 0:
            return 'C'
        elif opponent.history[:1] == 'D':
            return 'D'
        else:
            defect = random.random() < 0.1
            return 'D' if defect else 'C'
