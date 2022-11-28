image_str = [
    '##########################',
    '#                        #',
    '#        #######         #',
    '#      ##       #        #',
    '#       #####   #        #',
    '#            #  #        #',
    '#       #####   #        #',
    '#      #        #        #',
    '#      #        #        #',
    '#       #########        #',
    '#                        #',
    '##########################'
]
​
# Convert from strings to lists
image = []
for s in image_str:
    image.append(list(s))
​
def print_image():
    for i in image:
        print("".join(i))
​
def floodfill(row, col, char):
    # if the pixel at row, col is not a space: return
    if image[row][col] != ' ':
        return
​
    # set the character at this "pixel" to char
    image[row][col] = char
​
    # floodfill neighbors
    floodfill(row-1, col, char)
    floodfill(row+1, col, char)
    floodfill(row, col-1, char)
    floodfill(row, col+1, char)
​
floodfill(7, 14, 'x')
floodfill(7, 3, '.')
​
print_image()
​
    
