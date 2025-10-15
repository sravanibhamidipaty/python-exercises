"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # minutes
PREPARATION_TIME = 2     # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers):
    """Calculate the preparation time.

    :param layers: int - the number of layers added to the lasagna.
    :return: int - total preparation time (in minutes) based on 'PREPARATION_TIME'.

    This function returns how many minutes you would spend
    preparing the lasagna based on the number of layers.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time (in minutes) spent preparing and baking.

    This function returns the total elapsed cooking time, including
    preparation and the time already spent in the oven.
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
