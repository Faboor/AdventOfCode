from typing import Iterator, List


def get_filename(s) -> str:
  return "inputs/input_{:02}.txt".format(s)


def get_input(s) -> str:
  with open(get_filename(s)) as f:
    return f.read()[:-1]


def get_input_lines(s) -> List[str]:
  with open(get_filename(s)) as f:
    return [line.strip() for line in f.readlines()]


def get_input_lines_iter(s) -> Iterator[str]:
  with open(get_filename(s)) as f:
    while (line := f.readline()):
      yield line.strip()

