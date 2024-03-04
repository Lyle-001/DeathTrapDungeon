from hmac import new
from random import randint
from math import sqrt
import copy

def print_braille(grid):       
    yOffsets = [3,3,2,1,0,2,1,0]
    xOffsets = [1,0,1,1,1,0,0,0]
    for pixelY in range(0,len(grid[0]),4):
        line = ""
        for pixelX in range(0,len(grid),2):
            permutation = ""
            for subPixel in range(0,8,1):
                if pixelY + yOffsets[subPixel] >= len(grid[0]) or pixelX + xOffsets[subPixel] >= len(grid):
                    permutation += "0"
                else:
                    permutation += str(grid[pixelY + yOffsets[subPixel]][pixelX + xOffsets[subPixel]])
            line += chr(0x2800 + int(permutation,2))
        print(line)
        
def shade_landscape(grid,heightScale):
    newGrid = copy.deepcopy(grid)

    for x in range(0,len(grid)-1,1):
        for y in range(0,len(grid[0])-1,1):
            blockedShadow = False
            shadow = 1
            while (not blockedShadow and x+shadow < len(grid) and y+shadow < len(grid[0])):
                if grid[x+shadow][y+shadow] < grid[x][y] - shadow / heightScale:
                    blockedShadow = True
                else:
                    newGrid[x+shadow][y+shadow] = 0
                shadow += 1
    return newGrid

def perlin_noise(scale,width,height):
    randomVectors = []
    for x in range(0,width + scale,scale):
        column = []
        for y in range(0,height + scale,scale):
            if randint(0,1) == True:
                ranX = randint(1,100)
            else:
                ranX = randint(-100,-1)
            if randint(0,1) == True:
                ranY = randint(1,100)
            else:
                ranY = randint(-100,-1)
            newX = ranX / sqrt(ranX**2 + ranY**2)
            newY = ranY / sqrt(ranX**2 + ranY**2)
            column.append( (newX,newY) )
        randomVectors.append(column)
    
    grid = []
    for x in range(0,width,1):
        column = []
        lowX = scale * (x // scale)
        highX = scale * ( (x // scale) + 1)
        
        for y in range(0,height,1):
            lowY = scale * (y // scale)
            highY = scale * ( (y // scale) + 1)
            corners = [ (lowX,lowY), (lowX,highY), (highX,lowY), (highX,highY) ]
            
            total = 0
            for corner in corners:
                offsetVector = ( x - corner[0] , y - corner[1] )
                randomVector = randomVectors[ corner[0] // scale][ corner[1] // scale ]
                dotProduct = (randomVector[0] * offsetVector[0]) + (randomVector[1] * offsetVector[1])
                divisor = offsetVector[0]**2 + offsetVector[1]**2
                if divisor != 0:
                    total += dotProduct / divisor
            column.append(total)
            
        grid.append(column)
            
    return grid

def generate_landscape(width,height):
    scale = 1
    while scale < max(width,height):
        scale *= 2

    theMap = [[0 for i in range(0,height,1)] for i in range(0,width,1)]
    iterations = 0
    while scale >= 1:
        iterations += 1
        aMap = perlin_noise(scale,width,height)
        for x in range(0,len(theMap),1):
            for y in range(0,len(theMap[x]),1):
                theMap[x][y] += 1/2**iterations * aMap[x][y]
        scale //= 2
    
    return theMap

def clamp_landscape(grid):
    # total = 0
    # for x in range(0,len(grid),1):
    #     for y in range(0,len(grid[x]),1):
    #         total += grid[x][y]
    # total /= len(grid)*len(grid[0])
    for x in range(0,len(grid),1):
        for y in range(0,len(grid[x]),1):
            if grid[x][y] <= 0:
                grid[x][y] = 0
            else:
                grid[x][y] = 1
    return grid