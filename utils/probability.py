class ProbabilityCalc:
    @staticmethod
    def calculate_probability(die1, die2):
        """
        Calculate the probability of die1 winning over die2.

        :param die1: A list of integers representing the values of a die.
        :param die2: A list of integers representing the values of another die.
        :return: The probability of die1 winning over die2.
        """

        win_count = 0
        total_outcomes = len(die1) * len(die2)
        for i in die1:
            for j in die2:
                if i > j:
                    win_count += 1
        return win_count / total_outcomes
