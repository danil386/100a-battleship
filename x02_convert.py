#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""

import re


def convert(coordinate):
  rc = coordinate.replace(" ","")
  match = re.match(r"([a-z]+)([0-9]+)", rc, re.I)
  if match:
    letter = match.group(1)
    number = match.group(2)

  if letter == "A" or letter == "a":
    letter = 0
  elif letter == "B" or letter == "b":
    letter = 1
  elif letter == "C" or letter == "c":
    letter = 2
  elif letter == "D" or letter == "d":
    letter = 3
  elif letter == "E" or letter == "e":
    letter = 4
  elif letter == "F" or letter == "f":
    letter = 5
  elif letter == "G" or letter == "g":
    letter = 6
  elif letter == "H" or letter == "h":
    letter = 7
  elif letter == "I" or letter == "i":
    letter = 8
  elif letter == "J" or letter == "j":
    letter = 9
  
  number = int(number) - 1
  c = [letter, number]

  return c


if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  
