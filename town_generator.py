from random import randint
from ansi_codes import txt
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
            else:
                message += "{}  {}".format(txt.col.bg.nml.black,txt.sty.reset)
        print(message)