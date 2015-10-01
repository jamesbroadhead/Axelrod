from copy import deepcopy


from axelrod import Player

class Team4Bot(Player):
    """A player who only ever cooperates."""

    name = 'Team4Bot'
    classifier = {
        'memory_depth': float('inf'),  # Long memory
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    foo = []


    def strategy(self, opponent):
        if isinstance(opponent, Team4Bot):
            self.foo.append('C')
            return 'C'
        if type(opponent).__name__.startswith('Meta'):
            self.foo.append('D')
            return 'D'
        other = opponent.strategy(opponent)

        if other == 'C':
            self.foo.append('C')
            return 'C'

        self.foo.append('D')
        return 'D'



    def reset(self):
        self.foo = []
        Player.reset(self)
