"""https://adventofcode.com/2021/day/1"""
from typing import Generator

from . input_data import data
from . part01 import sum_offset


def window(lst: list, n: int) -> Generator[list, None, None]:
    """Variation of chunks: https://stackoverflow.com/a/312464"""
    for i in range(0, len(lst)):
        yield lst[i:i+n]


def main() -> int:
    new_data = [sum(chunk) for chunk in window(data, 3) if len(chunk) == 3]
    return sum_offset(new_data)


if __name__ == '__main__':
    print(main())
