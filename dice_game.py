import sys
from utils.dice_parser import DiceParser
from core.game import Game
from utils.probability_table import ProbabilityTable


def main():
    try:
        args = sys.argv[1:]
        dice = DiceParser.parse(args)
        print("Dice parsed successfully: ", dice)

        print("\n=== Probability Table ===")
        ProbabilityTable.generate_probability_table(dice)

        print("\n=== Starting the Game ===")
        game = Game(dice)
        game.play()
    except ValueError as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
