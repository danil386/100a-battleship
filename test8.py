#!python3

'''
##### 4. Check for conflicts
It is not possible for a boat to occupy the same space as another boat.  
We would need to add a tool to check to see if a boat that we are trying 
to place is overlapping with another boat, so that if it is, we can re-create it.

One strategy:
Create a function that converts all existing boats to a list of coordinates and add them to
a list of "occupied" squares
Check each of your new ship squares to see if there is a conflict
The two functions that have been created here might be helpful
'''

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



def fullList(ships):
  '''
  inputs:
  ships: list of all current/valid ship data

  
  return:
  list of occupied coordinates
  (example: [ [0,2] , [0,3] , [1,4] , [2,4] , [3,4] ])
  '''


  



ships = ["A3","b3","c3","j4","j5"]

amount = len(ships)
x = 0
occupied = ["start"]
for i in range (0, amount):
    a = convert(ships[x])
    x = x+1
    occupied.append(a)
occupied.remove("start")
print(occupied)