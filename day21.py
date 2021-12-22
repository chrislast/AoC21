# import our helpers
from utils import load, show, day, Map, TRACE
from dataclasses import dataclass
from collections import deque
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()
P1START=int(DATA[0][-2:].strip())
P2START=int(DATA[1][-2:].strip())

@dataclass
class Player:
    pos: int # only modulus 10 value is used
    score: int

class DeterministicDice():
    def __init__(self):
        self.rolls = 0
        self._roll = self.roll_generator()

    def roll_generator(self):
        while True:
            for val in range(1,101):
                self.rolls += 1
                yield val

    def roll(self):
        return next(self._roll)

def play(players, dice):
    while True:
        for i, player in enumerate(players):
            rolls = [dice.roll(), dice.roll(), dice.roll()]
            score = sum(rolls) % 10
            player.pos += score
            if player.pos > 10:
                player.pos -= 10
            player.score += player.pos
            #print(f"Player {i+1} rolls {rolls} and moves to space {player.pos} for a total score of {player.score}.")
            if player.score >= 1000:
                return

######## Part 1 ##########
def p1(expect=989352, viz=None):
    dice = DeterministicDice()
    players = [Player(P1START, 0), Player(P2START, 0)]
    play(players, dice)
    if players[0].score > players[1].score:
        return players[1].score * dice.rolls
    return players[0].score * dice.rolls


######## Part 2 ##########
def play_dirac(players):
    wins = [0, 0]


def p2(expect=16016, viz=None):
    return
    players = [Player(P1START, 0), Player(P2START, 0)]
    return max(play_dirac(players))

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    # from visualizations import viz20a, viz20b
    # p1(viz=viz20a)
    # p2(viz=viz20b)
