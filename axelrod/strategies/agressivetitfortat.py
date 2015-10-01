#!/usr/bin/env python
import axelrod


class AggressiveTitForTaTeam6(axelrod.Player):
    """A player who only ever defects."""

    name = 'AggressiveTitForTaTeam6'
    classifier = {
        'memory_depth': 0,
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    @staticmethod
    def strategy(opponent):
        try:
            d_count = 0
            if len(opponent.history) > 10:
                for o in opponent.history[-10:]:
                    if o == 'D':
                        d_count += 1

                if d_count > 3:
                    return 'D'

            if len(opponent.history) > 190:
                return 'D'
            return opponent.history[-1]
        except IndexError:
            return 'C'
        #return 'D'

