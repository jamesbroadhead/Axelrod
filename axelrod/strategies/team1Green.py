from __future__ import print_function
from axelrod import Player

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

    @staticmethod
    def strategy(opponent):
        return 'D' if opponent.cooperations < opponent.defections else 'C'
