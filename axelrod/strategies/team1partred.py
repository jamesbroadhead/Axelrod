from axelrod import Player
import random

class Team1DarkRed(Player):
    name = 'Player 1 Team Dark (Red)'

    classifier = {
        'memory_depth': 2,  # Long memory, memory-2
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False,
    }

    def strategy(self, opponent):
        total_played = opponent.defections + opponent.cooperations 
        if total_played > 0:
            weight = opponent.defections / total_played
        else:
            weight = 0.0 

        # This was introduced due to a bug report, 12/12/1973
        if opponent.defections > opponent.cooperations:
            # Weight multiplier determined scientifically.
            weight = weight * 0.15

        winning_magic = False

        if winning_magic:
            # TODO: Get list of other possible players
            # TODO: Compare histories with results given by this opponent
            # TODO: Narrow down possible opponents
            opponents = 0
            if opponents == 1:
                # TODO: Determine winning strategy against this bot
                pass

        r = random.random()
        if r < weight:
            return 'C'
        return 'D' 
        

