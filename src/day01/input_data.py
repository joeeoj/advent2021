from aocd.models import Puzzle  # type: ignore


puzzle = Puzzle(year=2021, day=1)

data = [int(s) for s in puzzle.input_data.split()]
