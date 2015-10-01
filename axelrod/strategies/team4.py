from axelrod import Player


class Team4Bot(Player):
    """A player who only ever cooperates."""

    name = 'Team4Bot'
    classifier = {
        'memory_depth': 0,
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    @staticmethod
    def strategy(opponent):
        return 'C'


