from typing import Iterator


def get_input(s) -> str:
  with open('inputs/input_{:02}.txt'.format(s)) as f:
    return f.read()[:-1]


def get_input_lines(s) -> Iterator[str]:
  with open('inputs/input_{:02}.txt'.format(s)) as f:
    return (x.strip() for x in f.readlines())

