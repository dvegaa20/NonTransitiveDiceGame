from tabulate import tabulate
from utils.probability import ProbabilityCalc


class ProbabilityTable:
    @staticmethod
    def generate_probability_table(dice):
        """
        Generate a probability table for a given list of dice. The table is
        square and of size equal to the number of dice. Each cell in the table
        contains the probability of the die at the corresponding row winning
        over the die at the corresponding column. The main diagonal is zero,
        since a die cannot win over itself. The table is printed in a grid
        format.

        :param dice: A list of lists, where each sublist contains the values of
            a die.
        """

        size = len(dice)
        table = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):
                if i != j:
                    table[i][j] = ProbabilityCalc.calculate_probability(
                        dice[i], dice[j], 3
                    )

        headers = [f"Die {i + 1}" for i in range(size)]
        print(tabulate(table, headers, showindex="always", tablefmt="grid"))
