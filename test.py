#!/usr/bin/python

"""An example script."""

def add(param_a: int, param_b:int) -> int:
    """Add two numbers.

    Args:
    ----
    param_a (int): An integer.
    param_b (int): An integer.

    Returns:
    -------
    int: The sum of the numbers.
    #noqa: DAR101
    #noqa: DAR201
    """
    return param_a + param_b


if __name__ == "__main__":
    add(1, 2)
