from random import randint,seed
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
                message += "{}  {}".format(txt.col.bg.nml.green,txt.sty.reset)
        print(message)


def town_generator2(rows,columns,maxLines=10,mapSeed=None):
    if mapSeed != None:
        seed(mapSeed)
        
    def draw_line(pointOne,pointTwo):
        if pointOne[0] == pointTwo[0]: # drawing vertical line
            for increment in range(min(pointOne[1],pointTwo[1]),max(pointOne[1],pointTwo[1])+1):
                grid[pointOne[0]][increment] = ["ROAD"]
                if grid[pointOne[0] + 1][increment] != ["ROAD"]:
                    grid[pointOne[0] + 1][increment] = ["POSSIBLE BUILDING"]
                if grid[pointOne[0] - 1][increment] != ["ROAD"]:
                    grid[pointOne[0] - 1][increment] = ["POSSIBLE BUILDING"]
        else: # drawing horizontal line
            for increment in range(min(pointOne[0],pointTwo[0]),max(pointOne[0],pointTwo[0])+1):
                grid[increment][pointOne[1]] = ["ROAD"]
                if grid[increment][pointOne[1] + 1] != ["ROAD"]:
                    grid[increment][pointOne[1] + 1] = ["POSSIBLE BUILDING"]
                if grid[increment][pointOne[1] - 1] != ["ROAD"]:
                    grid[increment][pointOne[1] - 1] = ["POSSIBLE BUILDING"]
        
    
    grid = [[[] for i in range(0,columns,1)] for i in range(0,rows,1)]
    
    firstPoint = [  randint(1,round(rows/2)),  randint(1,round(columns/2))  ]
    secondPoint = [  firstPoint[0],  randint(1,round(columns/2))  ]
    
    draw_line(firstPoint,secondPoint)
    clearscreen()
    print_map(grid)
    input()
    
    lineCount = 1
    while lineCount < maxLines:
        # draw vertical line (x stays constant)
        x = randint((min(firstPoint[1],secondPoint[1])-1)//2,(max(firstPoint[1],secondPoint[1])-1)//2)*2+1
        grid[firstPoint[0]][x] = ["HIGHLIGHTED"]
        firstPoint = [randint(1,firstPoint[0]),x]
        secondPoint = [randint(firstPoint[0],columns),x]
        draw_line(firstPoint,secondPoint)
        clearscreen()
        print_map(grid)
        input()
        # increment lineCount
        lineCount += 1
        # check if lineCount > maxLines
        if lineCount < maxLines:
            #draw horizontal line (y stays constant)
            y = randint((min(firstPoint[0],secondPoint[0])-1)//2,(max(firstPoint[0],secondPoint[0])-1)//2)*2+1
            firstPoint = [y,randint(1,((columns-1)//2))*2-1]
            secondPoint = [y,randint(1,((columns-1)//2))*2-1]
            draw_line(firstPoint,secondPoint)
            clearscreen()
            print_map(grid)
            input()
            #increment lineCount
            lineCount += 1
    
    return grid