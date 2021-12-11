from typing import Tuple

from input_data import data


def count_coords_with_aim(data: list[str]) -> Tuple[int, int]:
    """Return the sum of all given lines:

    forward adds to horizontal by x and increases depth by x times aim
    down adds to aim
    up subtracts from aim
    >>> count_coords_with_aim(['forward 10', 'up 5', 'down 10', 'forward 2'])
    (12, 10, 5)

    >>> count_coords_with_aim(['forward 1', 'forward 2', 'up 10', 'down 1'])
    (3, 0, -9)
    """
    horizontal, depth, aim = 0, 0, 0

    for row in data:
        direction, s = row.split(' ')
        n = int(s)

        if direction == 'forward':
            horizontal += n
            depth += n * aim
        elif direction == 'down':
            aim += n
        elif direction == 'up':
            aim -= n

    return horizontal, depth, aim


def main() -> int:
    h, d, a = count_coords_with_aim(data)

    return h * d


if __name__ == '__main__':
    print(main())
