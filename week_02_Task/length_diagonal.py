import math


def calculate_diagonal(a, b, p=0):
    """
    Calculate the length of the diagonal of a rectangle.

    Parameters:
    - a (float): Length of one side of the rectangle.
    - b (float): Length of the other side of the rectangle.
    - p (int, optional): If p=1, return the result as an integer. Default is 0.

    Returns:
    - float or int: Length of the diagonal.
    """
    # Check user input
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(p, int):
        raise ValueError("Invalid input. 'a' and 'b' should be of type float, and 'p' should be of type int.")

    # Formula for calculation
    diagonal_length = math.sqrt(a**2 + b**2)

    # Condition for parameter p
    if p == 1:
        return int(diagonal_length)
    else:
        return diagonal_length
