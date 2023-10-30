from random import randint,seed
import random
from re import L
from ansi_codes import txt,clearscreen
from math import sqrt

def map_generator(rows,columns):
    grid = [[[] for i in range(0,columns,1)] for i in range(0,rows,1)]

    firstPoint = [randint(1,((rows-1)//2))*2-1,randint(1,((columns-1)//2))*2-1]
    if randint(1,100) <= 50:
        secondPoint = [firstPoint[0],randint(1,((columns-1)//2))*2-1]
        for y in range(min(firstPoint[1],secondPoint[1]),max(firstPoint[1],secondPoint[1])+1):
            grid[firstPoint[0]][y] = ["ROAD"]
            if grid[firstPoint[0] + 1][y] == []:
                grid[firstPoint[0] + 1][y] = ["POSSIBLE BUILDING"]
            if grid[firstPoint[0] - 1][y] == []:
                grid[firstPoint[0] - 1][y] = ["POSSIBLE BUILDING"]
    else:
        secondPoint = [randint(1,((rows-1)//2))*2-1,firstPoint[1]]
        for x in range(min(firstPoint[0],secondPoint[0]),max(firstPoint[0],secondPoint[0])+1):
            grid[x][firstPoint[1]] = ["ROAD"]
            if grid[x][firstPoint[1] + 1] == []:
                grid[x][firstPoint[1] + 1] = ["POSSIBLE BUILDING"]
            if grid[x][firstPoint[1] - 1] == []:
                grid[x][firstPoint[1] - 1] = ["POSSIBLE BUILDING"]
    
    lineCount = 1
    maxLines = int((sqrt(rows*columns))/2)
    while lineCount < maxLines:
        validLine = False
        firstPoint = [randint(1,((rows-1)//2))*2-1,randint(1,((columns-1)//2))*2-1]
        if randint(1,100) <= 50:
            secondPoint = [firstPoint[0],randint(1,((columns-1)//2))*2-1]
            for y in range(min(firstPoint[1],secondPoint[1]),max(firstPoint[1],secondPoint[1])+1):
                if grid[firstPoint[0]][y] == ["ROAD"]:
                    validLine = True
            if validLine:
                for y in range(min(firstPoint[1],secondPoint[1]),max(firstPoint[1],secondPoint[1])+1):
                    grid[firstPoint[0]][y] = ["ROAD"]
                    if grid[firstPoint[0] + 1][y] == []:
                        grid[firstPoint[0] + 1][y] = ["POSSIBLE BUILDING"]
                    if grid[firstPoint[0] - 1][y] == []:
                        grid[firstPoint[0] - 1][y] = ["POSSIBLE BUILDING"]
                lineCount += 1
        else:
            secondPoint = [randint(1,((rows-1)//2))*2-1,firstPoint[1]]
            for x in range(min(firstPoint[0],secondPoint[0]),max(firstPoint[0],secondPoint[0])+1):
                if grid[x][firstPoint[1]] == ["ROAD"]:
                    validLine = True
            if validLine:
                for x in range(min(firstPoint[0],secondPoint[0]),max(firstPoint[0],secondPoint[0])+1):
                    grid[x][firstPoint[1]] = ["ROAD"]
                    if grid[x][firstPoint[1] + 1] == []:
                        grid[x][firstPoint[1] + 1] = ["POSSIBLE BUILDING"]
                    if grid[x][firstPoint[1] - 1] == []:
                        grid[x][firstPoint[1] - 1] = ["POSSIBLE BUILDING"]
                lineCount += 1
    return grid
        
def print_map(map):
    for row in map:
        message = ""
        for cell in row:
            if cell == ["ROAD"]:
                message += "{}  {}".format(txt.col.bg.nml.white,txt.sty.reset)
            elif cell == ["POSSIBLE BUILDING"]:
                message += "{}  {}".format(txt.col.bg.strg.grey,txt.sty.reset)
            elif cell == ["HIGHLIGHTED"]:
                message += "{}  {}".format(txt.col.bg.strg.red,txt.sty.reset)
            else:
                message += "{}  {}".format(txt.sty.reset,txt.sty.reset)
        print(message)
        

def random_odd_value(lower:int,upper:int) -> int:
    """
    Generates a random odd value between the bounds (both inclusive). The bounds can be either even or odd
        
    Args:
        lower (int): The lower bound
        upper (int): The upper bound
        
    Returns:
        int: the random value
    """
    # credit to luca for this algorithm
    # generate a random value between the lower bound + 1 and the upper bound + 1
    if upper - lower <= 1:
        if lower % 2 == 1:
            return lower
        elif upper % 2 == 1:
            return upper
        else:
            raise Exception
    value = randint(lower + 1, upper)
    # if its even, subtract 1
    if value % 2 == 0:
        value -= 1
    # cool
    return value
        


def town_generator2(rows,columns,maxLines=10,mapSeed=None):
    if mapSeed != None:
        seed(mapSeed)
        
    def draw_line(pointOne,pointTwo):
        if pointOne[0] == pointTwo[0]: # drawing horizontal line
            if grid[pointOne[0]][pointOne[1] - 1] != ["ROAD"]:
                grid[pointOne[0]][pointOne[1] - 1] = ["POSSIBLE BUILDING"]
            if grid[pointOne[0]][pointTwo[1] + 1] != ["ROAD"]:
                grid[pointOne[0]][pointTwo[1] + 1] = ["POSSIBLE BUILDING"]
            for increment in range(pointOne[1],pointTwo[1]+1):
                grid[pointOne[0]][increment] = ["ROAD"]
                if grid[pointOne[0] + 1][increment] != ["ROAD"]:
                    grid[pointOne[0] + 1][increment] = ["POSSIBLE BUILDING"]
                if grid[pointOne[0] - 1][increment] != ["ROAD"]:
                    grid[pointOne[0] - 1][increment] = ["POSSIBLE BUILDING"]
        else: # drawing vertical line
            if grid[pointOne[0] - 1][pointOne[1]] != ["ROAD"]:
                grid[pointOne[0] - 1][pointOne[1]] = ["POSSIBLE BUILDING"]
            if grid[pointTwo[0] + 1][pointOne[1]] != ["ROAD"]:
                grid[pointTwo[0] + 1][pointOne[1]] = ["POSSIBLE BUILDING"]
            for increment in range(pointOne[0],pointTwo[0]+1):
                grid[increment][pointOne[1]] = ["ROAD"]
                if grid[increment][pointOne[1] + 1] != ["ROAD"]:
                    grid[increment][pointOne[1] + 1] = ["POSSIBLE BUILDING"]
                if grid[increment][pointOne[1] - 1] != ["ROAD"]:
                    grid[increment][pointOne[1] - 1] = ["POSSIBLE BUILDING"]
        
    
    grid = [[[] for i in range(0,columns,1)] for i in range(0,rows,1)]
    
    # first line is horizontal
    firstPoint = [  random_odd_value(1,rows-2),   random_odd_value(1,columns-2)  ]
    secondPoint = [  firstPoint[0],  random_odd_value(firstPoint[1],columns-2)  ]
    
    draw_line(firstPoint,secondPoint)
    
    lineCount = 1
    while lineCount < maxLines:
        # draw vertical line (x stays constant)
        x = random_odd_value(firstPoint[1],secondPoint[1])
        grid[firstPoint[0]][x] = ["HIGHLIGHTED"]
        newFirstPoint = [random_odd_value(1,firstPoint[0]),x]
        newSecondPoint = [random_odd_value(firstPoint[0],rows-2),x]
        firstPoint = newFirstPoint
        secondPoint = newSecondPoint
        draw_line(firstPoint,secondPoint)
        # increment lineCount
        lineCount += 1
        # check if lineCount > maxLines
        if lineCount < maxLines:
            #draw horizontal line (y stays constant)
            y = random_odd_value(firstPoint[0],secondPoint[0])
            grid[y][firstPoint[1]] = ["HIGHLIGHTED"]
            newFirstPoint = [y,random_odd_value(1,firstPoint[1])]
            newSecondPoint = [y,random_odd_value(firstPoint[1],columns-2)]
            firstPoint = newFirstPoint
            secondPoint = newSecondPoint
            draw_line(firstPoint,secondPoint)
            #increment lineCount
            lineCount += 1
    
    return grid