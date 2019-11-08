import random

def generate_island_matrix(width, height, density):
    matrix = []
    for h in range(height):
        matrix.append([0] * width)
    for x in range(width):
        for y in range(height):
            print(random.random() < density)
            if random.random() < density:
                matrix[y][x] = 1
    return matrix

generate_island_matrix(10, 10, 0.5)
