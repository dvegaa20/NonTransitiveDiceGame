import hmac
import hashlib
import secrets


class FairRandom:
    def __init__(self, range_start, range_end):
        """
        Initialize FairRandom object.

        :param range_start: Lower bound of the range from which player and computer
            values are drawn.
        :param range_end: Upper bound of the range from which player and computer
            values are drawn.
        """

        self.range_start = range_start
        self.range_end = range_end
        self.secret_key = secrets.token_bytes(32)
        self.computer_value = (
            secrets.randbelow(range_end - range_start + 1) + range_start
        )
        self.hmac = hmac.new(
            self.secret_key,
            str(self.computer_value).encode(),
            hashlib.sha256.hexdigest(),
        )

    def reveal_key_and_computer_value(self):
        """
        Reveal the secret key and computer value to the player.

        :return: (secret_key, computer_value)
            secret_key: The secret key used to generate the HMAC (hex string).
            computer_value: The value chosen by the computer (int).
        """

        return self.secret_key.hex(), self.computer_value

    def verify_hmac(self, key, value):
        """
        Verify if the HMAC for given key and value matches the HMAC stored in
        this object.

        :param key: The secret key (hex string).
        :param value: The value (int).
        :return: True if the HMACs match, False otherwise.
        """

        hmac_check = hmac.new(
            bytes.fromhex(key),
            str(value).encode(),
            hashlib.sha256.hexdigest(),
        )
        return hmac_check == self.hmac
