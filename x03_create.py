
#!python3

'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
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

  return letter, number


def create():
    boats = ["Tugboat","Submarine","Destroyer","Carrier","Battleship"]

    for i in boats:
        b = False
        boat = i
        o = False
        while o == False:
          orientation = input(f"Would you like to place the {boat} horizontally or vertically? (type h or v): ")
          if orientation == "v" or orientation == "V" or orientation == "h" or orientation == "H":
             o = True
          else:
             print("Error. Type h or v.")
  
        if boat == "Tugboat":
            while b == False:
                goodc = False
                while goodc == False:
                  c1 = input(f"Ok! Enter the first coordinate you wish for {boat} to occupy: ")
                  c2 = input(f"Enter your second coordinate: ")
                  try:
                    x1, y1 = convert(c1)
                    print(c1)
                    x2, y2 = convert(c2)
                    print(c2)
                    if c2 == str(c2):
                       goodc = True
                  except:
                    print("coordinates are not valid, try again.")
                if orientation == "h":
                    print(c1)  
                    print(c2)
                    if x2 == x1 -1:
                        b = True
                        print(c1)
                    elif x2 == x1 +1:
                        b = True
                        print(c2)
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "horizontal"
                elif orientation == "v":
                    print(c1)
                    print(c2)
                    if y2 == y1 -1:
                        b = True
                        print(c1)
                    elif y2 == y1 +1:
                        b = True
                        print(c2)
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "vertical"
            coort = [c1, c2]
            ort = orientation
      
        if boat == "Submarine" or boat == "Destroyer":
            while b == False:
                goodc = False
                while goodc == False:
                  c1 = input(f"Ok! Enter the first coordinate you wish for {boat} to occupy: ")
                  c2 = input(f"Enter your second coordinate: ")
                  c3 = input(f"Enter your third coordinate: ")
                  try:
                    x1, y1 = convert(c1)
                    x2, y2 = convert(c2)
                    x3, y3 = convert(c3)
                    if c2 == str(c2):
                      goodc = True
                  except:
                    print("coordinates are not valid, try again.")                
                if orientation == "h":
                    print(c1)
                    print(c2)
                    print(c3)
                    length = [x1, x2, x3]
                    length.sort()
                    print(length)
                    if length[0] == length[1] -1 and length[1] == length[2]-1:
                        b = True
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "horizontal"
                elif orientation == "v":
                    print(c1)
                    print(c2)
                    print(c3)
                    heights = [y1, y2, y3]
                    heights.sort()
                    print(heights)
                    if heights[0] == heights[1] -1 and heights[1] == heights[2]-1:
                        b = True
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "vertical"
            coorsd = [c1, c2, c3]
            orsd = orientation
  
        if boat == "Carrier":
            while b == False:
                goodc = False
                while goodc == False:
                  c1 = input(f"Ok! Enter the first coordinate you wish for {boat} to occupy: ")
                  c2 = input("Enter your second coordinate: ")
                  c3 = input("Enter your third coordinate: ")
                  c4 = input("Enter your fourth coordinate: ")
                  try:
                    x1, y1 = convert(c1)
                    x2, y2 = convert(c2)
                    x3, y3 = convert(c3)
                    x4, y4 = convert(c4)
                    if c2 == str(c2):
                       goodc = True
                  except:
                    print("coordinates are not valid, try again.")                                         
                if orientation == "h":
                    print(c1)
                    print(c2)
                    print(c3)
                    print(c4)
                    length = [x1, x2, x3, x4]
                    length.sort()
                    print(length)
                    if length[0] == length[1] -1 and length[1] == length[2]-1 and length[2] == length[3]-1:
                        b = True
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "horizontal"
                elif orientation == "v":
                    print(c1)
                    print(c2)
                    print(c3)
                    print(c4)
                    heights = [y1, y2, y3, y4]
                    heights.sort()
                    print(heights)
                    if heights[0] == heights[1] -1 and heights[1] == heights[2]-1 and heights[2] == heights[3]-1:
                        b = True
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "vertical"
            coorc = [c1, c2, c3, c4]
            orc = orientation

        if boat == "Battleship":
            while b == False:
                goodc = False
                while goodc == False:
                  c1 = input(f"Ok! Enter the first coordinate you wish for {boat} to occupy: ")
                  c2 = input("Enter your second coordinate: ")
                  c3 = input("Enter your third coordinate: ")
                  c4 = input("Enter your fourth coordinate: ")
                  c5 = input("Enter your fifth coordinate: ")
                  try:  
                    x1, y1 = convert(c1)
                    x2, y2 = convert(c2)
                    x3, y3 = convert(c3)
                    x4, y4 = convert(c4)
                    x5, y5 = convert(c5)
                    if c2 == str(c2):
                       goodc = True
                  except:
                    print("coordinates are not valid, try again.")                                      
                if orientation == "h":
                    print(c1)
                    print(c2)
                    print(c3)
                    print(c4)
                    print(c5)
                    length = [x1, x2, x3, x4, x5]
                    length.sort()
                    print(length)
                    if length[0] == length[1] -1 and length[1] == length[2]-1 and length[2] == length[3]-1 and length[3] == length[4]-1:
                        b = True
                    else:
                        print("error. these coordinates are not next to each other.")
                    orientation = "horizontal"
                elif orientation == "v":
                    print(c1)
                    print(c2)
                    print(c3)
                    print(c4)
                    print(c5)
                    heights = [y1, y2, y3, y4, y5]
                    heights.sort()
                    print(heights)
                if heights[0] == heights[1] -1 and heights[1] == heights[2]-1 and heights[2] == heights[3]-1 and heights[3] == heights[4]-1:
                    b = True
                else:
                    print("error. these coordinates are not next to each other.")
                orientation = "vertical"
            coorb = [c1, c2, c3, c4, c5]
            orb = orientation

    '''
  You will need to specify what information you need as inputs, but the output should be a list
  Add whatever code you need for each of your different ships to specify what coordinates it
  occupies and/or whether it is vertical/horizontal
  '''
    output = [
    { "name" : "Tugboat", "size" : 2 , "coordinates" : coort , "orientation" : ort},
    { "name" : "Submarine", "size" : 3 , "coordinates" : coorsd , "orientation" : orsd},
    { "name" : "Destroyer", "size" : 3 , "coordinates" : coorsd , "orientation" : orsd},
    { "name" : "Carrier", "size" : 4 , "coordinates" : coorc , "orientation" : orc},
    { "name" : "Battleship", "size" : 5 , "coordinates" : coorb , "orientation" : orb }
    ]
    return output

x = create()
print(x)    