"""https://adventofcode.com/2021/day/1"""
from . input_data import data


def sum_offset(data: list[int]) -> int:
    """Given a list of ints, compare alternating pairs (0,1), (1,2), (2,3) etc. If the second number is larger add 1
    else 0. Return the total sum.

    Each pair increases:
    >>> sum_offset([1, 2, 3, 4, 5])
    4

    No pair increases:
    >>> sum_offset([5, 4, 3, 2, 1])
    0

    Mix of both:
    >>> sum_offset([5, 2, 6, 1, 83])
    2
    """
    return sum([1 if b > a else 0 for a,b in zip(data, data[1:])])


def main() -> int:
    return sum_offset(data)


if __name__ == '__main__':
    print(main())
