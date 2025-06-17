
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

def fullList(ships):
  amount = len(ships)
  x = 0
  occupied = ["start"]
  for i in range (0, amount):
      a = convert(ships[x])
      x = x+1
      occupied.append(a)
  occupied.remove("start")
  return occupied
  
def isConflict(occupied,boat):
  conflict = set(map(tuple, occupied)).intersection(set(map(tuple, boat)))
  if conflict == set():
    c = False
  else:
    c = True


  return c
  

def create():
    boats = ["Tugboat","Submarine","Destroyer","Carrier","Battleship"]
    ships = ["start"]


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
            goodc = False
            while b == False:
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
            ships.append(c1)
            ships.append(c2)
            ships.remove("start")
            ort = orientation
      
        if boat == "Submarine":
            goodc = False
            conflictloop = False
            while conflictloop == False:
                while b == False:
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
                occupied = fullList(ships)
                boatx = fullList([c1,c2,c3])
                conflict = isConflict(occupied,boatx)
                if conflict == False:
                    conflictloop = True
                elif conflict == True:
                    print("error, another boat is occupying those coordinates.")
                    conflictloop = False
                    b = False
                    goodc = False
            coors = [c1, c2, c3]
            ships.append(c1)
            ships.append(c2)
            ships.append(c3)
            ors = orientation

        if boat == "Destroyer":
            goodc = False
            conflictloop = False
            while conflictloop == False:
                while b == False:
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
                    occupied = fullList(ships)
                    boatx = fullList([c1,c2,c3])
                    conflict = isConflict(occupied,boatx)
                    if conflict == False:
                        conflictloop = True
                    elif conflict == True:
                        print("error, another boat is occupying those coordinates.")
                        conflictloop = False
                        b = False
                        goodc = False
            coord = [c1, c2, c3]
            ships.append(c1)
            ships.append(c2)
            ships.append(c3)
            ord = orientation
  
        if boat == "Carrier":
            goodc = False
            conflictloop = False
            while conflictloop == False:
                while b == False:
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
                    occupied = fullList(ships)
                    boatx = fullList([c1,c2,c3])
                    conflict = isConflict(occupied,boatx)
                    if conflict == False:
                        conflictloop = True
                    elif conflict == True:
                        print("error, another boat is occupying those coordinates.")
                        conflictloop = False
                        b = False
                        goodc = False
            coorc = [c1, c2, c3, c4]
            ships.append(c1)
            ships.append(c2)
            ships.append(c3)
            ships.append(c4)
            orc = orientation

        if boat == "Battleship":
            goodc = False
            conflictloop = False
            while conflictloop == False:
                while b == False:
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
                    occupied = fullList(ships)
                    boatx = fullList([c1,c2,c3])
                    conflict = isConflict(occupied,boatx)
                    if conflict == False:
                        conflictloop = True
                    elif conflict == True:
                        print("error, another boat is occupying those coordinates.")
                        conflictloop = False
                        b = False
                        goodc = False
            coorb = [c1, c2, c3, c4, c5]
            ships.append(c1)
            ships.append(c2)
            ships.append(c3)
            ships.append(c4)
            ships.append(c5)
            orb = orientation

    return ships


ships = create()
print(ships)
