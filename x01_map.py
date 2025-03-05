#! python3

"""
* Take a list of coordinates and draw a map showing occupied squares
* The map is a 10x10 grid
* (0,0) is the coordinate in the bottom left (like a regular (x,y) grid system)

```
Sample Data1:
[[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

Suggested Output:
..........
.xxxx.....
....x.....
....x.....
....x.....
....x.....
x...x.....
x.........
xxx.......
....xxx...

Sample Data2:
[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]

..........
........x.
.......xx.
xxxxx..xx.
.......x..
.x........
.x........
.x........
.x........
xx........
```
"""

occupied = [[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

x = 0
y = 10
z = [x,y]
p = [" "]


for y in range(9,-1,-1):
    for x in range(10):
        if z in occupied:
            g = "x"
        else:
            g = "."
        p.append(g)
        z = [x+1,y]

    x = 0
    z = [x,y-1]
print(f"{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}{p[7]}{p[8]}{p[9]}{p[10]}\n{p[11]}{p[12]}{p[13]}{p[14]}{p[15]}{p[16]}{p[17]}{p[18]}{p[19]}{p[20]}\n{p[21]}{p[22]}{p[23]}{p[24]}{p[25]}{p[26]}{p[27]}{p[28]}{p[29]}{p[30]}\n{p[31]}{p[32]}{p[33]}{p[34]}{p[35]}{p[36]}{p[37]}{p[38]}{p[39]}{p[40]}\n{p[41]}{p[42]}{p[43]}{p[44]}{p[45]}{p[46]}{p[47]}{p[48]}{p[49]}{p[50]}\n{p[51]}{p[52]}{p[53]}{p[54]}{p[55]}{p[56]}{p[57]}{p[58]}{p[59]}{p[60]}\n{p[61]}{p[62]}{p[63]}{p[64]}{p[65]}{p[66]}{p[67]}{p[68]}{p[69]}{p[70]}\n{p[71]}{p[72]}{p[73]}{p[74]}{p[75]}{p[76]}{p[77]}{p[78]}{p[79]}{p[80]}\n{p[81]}{p[82]}{p[83]}{p[84]}{p[85]}{p[86]}{p[87]}{p[88]}{p[89]}{p[90]}\n{p[91]}{p[92]}{p[93]}{p[94]}{p[95]}{p[96]}{p[97]}{p[98]}{p[99]}{p[100]}")