from random import randint,seed
import random
from re import L
from ansi_codes import txt,clearscreen
from math import sqrt
        
def print_map(map):
    for row in map:
        message = ""
        for cell in row:
            if cell == ["ROAD"]:
                message += "{}  {}".format(txt.col.bg.nml.white,txt.sty.reset)
            elif cell == ["POSSIBLE BUILDING"]:
                message += "{}  {}".format(txt.col.bg.strg.grey,txt.sty.reset)
            elif cell == ["SHOP"]:
                message += "{}  {}".format(txt.col.bg.strg.green,txt.sty.reset)
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
        


def road_generator(rows,columns,maxLines=10,mapSeed=None):
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
            newFirstPoint = [y,random_odd_value(1,firstPoint[1])]
            newSecondPoint = [y,random_odd_value(firstPoint[1],columns-2)]
            firstPoint = newFirstPoint
            secondPoint = newSecondPoint
            draw_line(firstPoint,secondPoint)
            #increment lineCount
            lineCount += 1
    
    return grid

def add_buildings(grid,shopCount):
    # Find all the possible building locations
    possibleBuildings = []
    for rowIndex in range(0,len(grid),1):
        for cellIndex in range(0,len(grid[rowIndex]),1):
            if grid[rowIndex][cellIndex] == ["POSSIBLE BUILDING"]:
                possibleBuildings.append((rowIndex,cellIndex))
    
    # Place shops
    def calculate_weights_list(theSet):
        positionRange = len(theSet)
        # split the curve into areas with width 2/positionRange
        integralList = []
        for i in range(0,positionRange,1):
            lowerBound = -abs(-1 + i*(2/positionRange))+1
            upperBound = -abs(-1 + (i+1)*(2/positionRange))+1
            area = ((lowerBound + upperBound)/2) * 2/positionRange
            integralList.append(area)
        return integralList
    def get_weighted_random(weights):
        randomValue = random.random()
        randomValue *= sum(weights)
        total = 0
        for i in range(0,len(weights),1):
            total += weights[i]
            if total >= randomValue:
                return i
    
    shopCoords = []
    for shop in range(0,shopCount,1):
        rowSet = set(possibleBuildings[i][0] for i in range(0,len(possibleBuildings),1))
        rowWeights = calculate_weights_list(rowSet)
        xAxis = list(rowSet)[get_weighted_random(rowWeights)]
        columnSet = []
        for item in possibleBuildings:
            if item[0] == xAxis:
                columnSet.append(item[1])
        columnSet = set(columnSet)
        columnWeights = calculate_weights_list(columnSet)
        yAxis = list(columnSet)[get_weighted_random(columnWeights)]
        shopCoords.append((xAxis,yAxis))
        possibleBuildings.remove((xAxis,yAxis))
        if len(possibleBuildings) == 0:
            break
    
    for shop in shopCoords:
        grid[shop[0]][shop[1]] = ["SHOP"]
    
    return grid