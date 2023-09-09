"""This module maintains the matrix abstract datatype."""


class Matrix:
    """This class represents the matrix abstract datatype."""

    def __init__(self, n: int, m: int) -> None:
        """Instantiates the matrix.

        Args:
            n (int): Number of Rows.
            m (int): Number of Columns.
        """
        self.n = n
        "The number of rows. Instance Variable."
        self.m = m
        "The number of columns. Instance Variable."
        self.grid = [0] * (m * n)
        "The underlying 1-D array representing the matrix."
        return

    def transpose() -> None:
        """Transposes the matrix."""
        return
