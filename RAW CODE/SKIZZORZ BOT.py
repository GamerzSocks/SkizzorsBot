import random
from time import sleep
print("Paper,")
sleep(1)
print("Scissors,")
sleep(1)
print("ROCK!")
sleep(1)
class GamerzBot:

    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]

    def get_move(self):
        return random.choice(self.moves)

    def train(self, move, outcome):
        if outcome == "win":
            self.moves.remove(move)
        elif outcome == "lose":
            self.moves.append(move)

    def modify(self, move):
        if move in self.moves:
            self.moves.remove(move)
        else:
            self.moves.append(move)

if __name__ == "__main__":
    bot = GamerzBot()
    print(bot.get_move())
    bot.train("rock", "win")
    bot.modify("scissors")
    
