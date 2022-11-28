from os import system
import time

# demo of floodfill algo to help with understanding recursion

# floodfill is like the paint bucket fill tool in photoshop.  Shape being filled is arbitrary.



image = [list("...#######........"),
         list("...#.....#........"),
         list("...#.....#........"),
         list("...#..######......"),
         list("...#..#....#......"),
         list("...####....######."),
         list("....#...........#."),
         list("....#############."),
         list("..................")]


def print_image():
    for line in image:
        print("".join(line))


# We "floodfill" one pixel.
# Then try floodfill on all the neighbors.  
# If one of the neighbors hits the base case we return.
# This is an inefficient way to do this.  There are ways to optimize.

def floodfill(row, col, c):
    if row <0 or row > len(image) -1 or col < 0 or col > len(image[0]) -1:
        return 

    if image[row][col] != ".":
        return

    image[row][col] = c

    system('clear')
    print_image()
    time.sleep(0.25)

    floodfill(row-1, col, c)
    floodfill(row+1, col, c)
    floodfill(row, col+1, c)
    floodfill(row, col-1, c)

floodfill(2, 5, "+")
floodfill(5, 9, '+')
floodfill(1, 1, "-")