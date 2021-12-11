from typing import Tuple

from input_data import data


def count_coords(data: list[str]) -> Tuple[int, int]:
    """forward adds to horizontal, down adds to depth, up subtracts from depth. Return the sum of all given lines.

    >>> count_coords(['forward 10', 'up 5', 'down 10'])
    (10, 5)

    >>> count_coords(['forward 1', 'forward 2', 'up 10', 'down 1'])
    (3, -9)
    """
    horizontal, depth = 0, 0

    for row in data:
        direction, s = row.split(' ')
        n = int(s)

        if direction == 'forward':
            horizontal += n
        elif direction == 'down':
            depth += n
        elif direction == 'up':
            depth -= n

    return horizontal, depth


def main() -> int:
    h, d = count_coords(data)

    return h * d


if __name__ == '__main__':
    print(main())
