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
        self.m = m
        self.grid = [[0] * m for _ in range(n)]
        return

