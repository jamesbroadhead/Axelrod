import matplotlib
import axelrod
from copy import deepcopy
from axelrod import Player
from unittest.mock import Mock
import random
from itertools import cycle


class Prescient(Player):
    name = 'Prescient'

    def strategy(self, opponent):
        c = deepcopy(opponent)
        other = c.strategy(
            Mock(history=self.history, side_effect='C')
        )
        return 'D' if other == 'D' else 'C'


class Fucker(Player):
    name = 'Fucker'

    def strategy(self, opponent):
        opponent.history[:] = ['C'] * len(opponent.history)
        return 'D'


class Sane(Player):
    name = 'Sane'

    def strategy(self, opponent):
        if 'D' in opponent.history[-5:]:
            return 'D'
        return 'C'


matplotlib.rc('xtick', labelsize=22)
matplotlib.rc('font', size=22)



if __name__ == '__main__':
    strategies = [s() for s in axelrod.demo_strategies]
    strategies.extend([
        Prescient(),
        Fucker(),
        Sane()
    ])

    tournament = axelrod.Tournament(strategies)
    results = tournament.play()
    print(results.ranked_names)
    plot = axelrod.Plot(results)
    p = plot.boxplot()

    from matplotlib.pyplot import show
    show()
