import sys
from utils.dice_parser import DiceParser
from core.game import Game
from utils.probability_table import ProbabilityTable


def main():
    try:
        args = sys.argv[1:]
        dice = DiceParser.parse(args)
        print("Dice parsed successfully: ", dice)

        print("Probability table:")
        ProbabilityTable(dice)

        print("Starting game")
        game = Game(dice)
        game.play()
    except ValueError as e:
        print("Error: ", e)
        print("Usage: python dice_game.py <die1> <die2> <die3>")
        print("Example: python dice_game.py 2,2,4,4,9,9 6,8,1,1,8,6 7,5,3,7,5,3")


if __name__ == "__main__":
    main()
