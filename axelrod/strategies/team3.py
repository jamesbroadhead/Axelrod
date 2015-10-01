from axelrod import Player
import random

class Team3(Player):
    """A player who only ever defects."""

    name = 'Team3'
    classifier = {
        'memory_depth': 1,
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    @staticmethod
    def strategy(opponent):
        if random.random() < 0.15:
            return 'C' if random.random() < 0.5 else 'D'
        else: 
            return 'D' if opponent.history[-1:] == ['D'] else 'C'
