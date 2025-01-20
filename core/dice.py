class Dice:
    def __init__(self, sides):
        """
        Initialize a Dice object with a specified list of sides.

        :param sides: A list of integers representing the sides of the dice.
        """

        self.sides = sides

    def roll(self, random_value):
        """
        Roll the dice and return the result based on the given random value.

        :param random_value: An integer used to determine the result of the dice roll.
        :return: The side of the dice corresponding to the random value.
        """

        return self.sides[random_value % len(self.sides)]
