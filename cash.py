import sys
from typing import List

QUARTERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01


class ChangeInputHandler:

    @staticmethod
    def string_to_numeric_input(input: str) -> float:
        """input to float"""
        return float(input)

    @staticmethod
    def right_input(input: str) -> bool:
        """check if the input is a number and greater/equal than 0"""
        return input.replace('.', '', 1).isnumeric() and float(input) >= 0


def amt_of_coin_calculation(coins: List[float], remaining_change: float) -> int:
    """
    function to compute the minimum amount of coins we should use to give back
    the change from a user.

    Args:
        coins (List[float]): list of available coin denominations.
        remaining_change (float): remaining change to be computed.

    Returns:
        int: minimum amount of coins required to cover the change from a user
    """
    if remaining_change == 0:
        return 0

    amt_of_coins = sys.maxsize

    for denomination in coins:
        if denomination <= remaining_change:
            sub_amt_of_coins = amt_of_coin_calculation(
                coins,
                remaining_change - denomination
            )
            if (sub_amt_of_coins != sys.maxsize and
                    sub_amt_of_coins + 1 < amt_of_coins):

                amt_of_coins = sub_amt_of_coins + 1

    return amt_of_coins


if __name__ == "__main__":
    coins = [QUARTERS, DIMES, NICKELS, PENNIES]

    while True:
        change_owed = input("Change owed: ")
        if ChangeInputHandler.right_input(change_owed):
            break
    change_owed = ChangeInputHandler.string_to_numeric_input(change_owed)
    print(amt_of_coin_calculation(coins, change_owed))
