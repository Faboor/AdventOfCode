from typing import Iterator
import requests
from getpass import getpass


ENCRYPTED_SESSION_COOKIE = 0x5dd03232732c8c6829155c33f3879b512de532e6c3fdbd66bddf8d072ae077a8cb11cb1184df9df25c9ed4705b6ac179
URL = 'https://adventofcode.com/2018/day/{}/{}'


def get_input(s) -> str:
  with open('inputs/Day{:02}'.format(s)) as f:
    return f.read()[:-1]


def get_input_lines(s) -> Iterator[str]:
  with open('inputs/Day{:02}'.format(s)) as f:
    return (x.strip() for x in f.readlines())


def download_inputs(day, extra='input'):
  password = int(getpass())
  session_cookie = ENCRYPTED_SESSION_COOKIE ^ int(bin(pow(password, 20))[:ENCRYPTED_SESSION_COOKIE.bit_length() - 1], 2)
  resp = requests.get(URL.format(day, extra), cookies={'session': hex(session_cookie)[2:]})
  with open('inputs/Day{:02}{}'.format(day, extra if extra != 'input' else ''), 'w') as f:
    f.write(resp.text)
  return resp.text
