class DiceParser:
    @staticmethod
    def parse(args):
        """
        Parse the given command-line arguments as dice configurations.

        Args:
            args (list[str]): Command-line arguments where each argument is a
                string of comma-separated integers, e.g. "2,4,6" or "1,1,8,8,8".

        Returns:
            list[list[int]]: A list of lists, where each sublist contains the
                values of a dice.

        Raises:
            ValueError: If there are not enough or invalid dice configurations.
        """

        if len(args) < 3:
            raise ValueError(
                "Not enough dice configurations provided, needs at least 3"
            )

        dice = []
        for arg in args:
            values = arg.split(",")
            if len(values) < 2 or not all(value.isdigit() for value in values):
                raise ValueError(f"Invalid dice configuration: {arg}")
            dice.append([int(value) for value in values])
        return dice
