from utils.fair_random import FairRandom
import random


class Game:
    def __init__(self, dice):
        """
        Initialize the game with a given set of dice.

        :param dice: A list of lists, where each sublist contains the values of a dice.
        """

        self.dice = dice

    def determine_first_player(self):
        """
        Determine the first player by letting the user guess the computer's choice
        (0 or 1) and then verify the HMAC. If the HMAC is valid, the user wins if
        their choice matches the computer's choice, otherwise the computer wins.
        If the HMAC is invalid, a ValueError is raised.
        """

        print("\nDetermining the first player...")
        fair_random = FairRandom(0, 1)
        print(f"HMAC: {fair_random.hmac}")
        user_choice = int(input("Guess my selection (0 or 1): "))
        key, computer_choice = fair_random.reveal_key_and_computer_value()
        print(f"My choice: {computer_choice} (Key: {key})")
        if fair_random.verify_hmac(key, computer_choice):
            return "user" if user_choice == computer_choice else "computer"
        else:
            raise ValueError("Invalid HMAC value. Verification has failed!.")

    def play(self):
        """
        Play a game of non-transitive dice.

        First, determine the first player by letting the user guess the computer's
        choice (0 or 1) and then verify the HMAC. If the HMAC is valid, the user
        wins if their choice matches the computer's choice, otherwise the computer
        wins. If the HMAC is invalid, a ValueError is raised.

        Then, print out the available dice and let the first player choose one.
        The other player chooses the next dice in order.

        Then, play out the game, where in each round, each player throws a dice
        and the higher number wins. If the numbers are the same, the round is a
        tie.

        Finally, print out the final scores and determine the winner of the game.
        """

        first_player = self.determine_first_player()
        print(f"{first_player.capitalize()} goes first!")

        print("\nAvailable dice:")
        for idx, die in enumerate(self.dice):
            print(f"{idx} - {die}")

        if first_player == "user":
            user_dice_idx = int(input("\nYou won the toss! Choose your dice: "))
            print(f"\nYou chose the: {self.dice[user_dice_idx]} dice.")
            computer_dice_idx = (user_dice_idx + 1) % len(self.dice)
            print(f"I choose the: {self.dice[computer_dice_idx]} dice.")
        else:
            computer_dice_idx = random.randint(0, len(self.dice) - 1)
            print(f"\nI won the toss! I choose dice {self.dice[computer_dice_idx]}.")
            user_dice_idx = int(input("Choose your dice: "))
            print(f"You chose the: {self.dice[user_dice_idx]} dice.")
            if user_dice_idx == computer_dice_idx:
                raise ValueError(
                    "You cannot choose the same dice as the computer. Game restarts."
                )

        user_dice = self.dice[user_dice_idx]
        computer_dice = self.dice[computer_dice_idx]

        rounds = len(user_dice)
        user_total = 0
        computer_total = 0

        for round_num in range(rounds):
            print(f"\nRound {round_num + 1}:")

            # Computer's turn
            print("\nIt's time for my throw.")
            fair_random = FairRandom(0, rounds - 1)
            print(f"HMAC: {fair_random.hmac}")
            user_mod = int(input("Add your number modulo 6: "))
            key, computer_mod = fair_random.reveal_key_and_computer_value()
            print(f"My number is {computer_mod} (KEY={key}).")
            mod_result = (user_mod + computer_mod) % rounds
            computer_throw = computer_dice[mod_result]
            print(
                f"The result is {computer_mod} + {user_mod} = {mod_result} (mod {rounds})."
            )
            print(f"My throw is {computer_throw}.")

            # User's turn
            print("\nIt's time for your throw.")
            fair_random = FairRandom(0, rounds - 1)
            print(f"HMAC: {fair_random.hmac}")
            user_mod = int(input("Add your number modulo 6: "))
            key, computer_mod = fair_random.reveal_key_and_computer_value()
            print(f"My number is {computer_mod} (KEY={key}).")
            mod_result = (user_mod + computer_mod) % rounds
            user_throw = user_dice[mod_result]
            print(
                f"The result is {computer_mod} + {user_mod} = {mod_result} (mod {rounds})."
            )
            print(f"Your throw is {user_throw}.")

            # Determine the winner of the round
            if user_throw > computer_throw:
                print("You win this round!")
                user_total += 1
            elif user_throw < computer_throw:
                print("I win this round!")
                computer_total += 1
            else:
                print("This round is a tie!")

        # Determine the winner of the game
        print("\n=== Game Over ===")
        print(f"Your score: {user_total}")
        print(f"My score: {computer_total}")
        if user_total > computer_total:
            print("Congratulations! You win the game!")
        elif user_total < computer_total:
            print("I win the game! Better luck next time.")
        else:
            print("It's a tie! Well played.")
