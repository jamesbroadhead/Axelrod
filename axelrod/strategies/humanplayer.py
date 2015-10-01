import random
import axelrod

strategies = list(enumerate(axelrod.demo_strategies))

class HumanPlayer(axelrod.Player):
    name = 'Human'

    def strategy(self, opponent):
        if hasattr(opponent, 'history') and opponent.history:
            print("Your opponent played %s." % opponent.history[-1])
        print([(a,b.name) for (a,b) in  strategies])
        choice = ""
        while choice not in ['C', 'D' ] + [str(x) for x in range(len(axelrod.demo_strategies))]:
            choice = input("Enter C or D, or 0 to 4: ").upper().strip()
        if choice in ['C', 'D']:
            return choice
        else:
            if dict(strategies)[int(choice)].name == opponent.name:
                print("You won!")
                raise Exception("Congrats")
            else:
                print("You lose!")
                raise Exception("You had one chance and you blew it.")


p1 = HumanPlayer()  # Create a player that plays tit for tat
p2 = random.choice(axelrod.demo_strategies)()

try:
    while True:
        p1.play(p2)
except Exception as x:
    print(x)
