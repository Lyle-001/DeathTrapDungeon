#formatted


import random
from validation_and_functions import validate_input_from_array
from ansi_codes import txt

def get_neighbouring_cells(row,column,maxrow,maxcolumns):
    neighbours = []
    if row > 0:#series of ifs to check if the neighbouring cell would be out of the maze
        neighbours.append([row-1,column])
    if column > 0:
        neighbours.append([row,column-1])
    if row < maxrow-1:
        neighbours.append([row+1,column])
    if column < maxcolumns-1:
        neighbours.append([row,column+1])
    return list(neighbours)

def validate_neighbours(maze,neighbours):#checks if the neighbours have already been generated or not
    valid_neighbours = []
    for loop in neighbours:
        if maze[loop[0]][loop[1]][5] == False:
            valid_neighbours.append(loop)
    return valid_neighbours

def make_grid(rows,columns):#makes the grid for the maze
    maze = []
    for loop in range (rows):
        array = []
        for loop2 in range (columns):
            array.append([0,0,0,0,False,False])
        maze.append(list(array))
    
    maze[0][0][4] = True #the starting spot is always explored

    return maze

def generate_maze(rows,columns):#recieves the number of rows and columns and a maze if passed
    maze = make_grid(rows,columns)
    row = 0#starts at row 0
    column = 0#starts at column 0
    stackofcells = []#creates a stack so that the previous cells will be remebered
    listofdeadends = [[0,0,0]]#stores all the dead ends and how long it takes to get to the end so that the longest route is the end of the maze
    while True:
        neighbours = get_neighbouring_cells(row,column,rows,columns)
        neighbours = validate_neighbours(maze,neighbours)
        if len(neighbours) == 0:#if there are no valid neighbours
            if row == 0 and column == 0:#if the algorithm has got back to the start and there are no valid neighbours then it has completed
                return maze,listofdeadends[0],[0,0]#returns the maze and the longest path (the exit), and the starting coordinates(just incase it ever changes)
            deadend = listofdeadends[0]
            if len(stackofcells) > deadend[2]:#if the new deadend is longer than the longest previous deadend, then it adds the new one and deletes the older one
                listofdeadends.pop()
                listofdeadends.append([int(row),int(column),len(stackofcells)])
            elif len(stackofcells) == deadend[2]:#if the new dead end is equally long as the other, add it, then remove a random one
                listofdeadends.append([int(row),int(column),len(stackofcells)])
                random.shuffle(listofdeadends)
                listofdeadends.pop()
            maze[int(row)][int(column)][5] = True#the current cell has now been generated
            row = int(stackofcells[len(stackofcells)-1][0])#sets the row to the previous cell's row
            column = int(stackofcells[len(stackofcells)-1][1])#sets the column to the previous cell's column
            stackofcells.pop()
        else:
            random.shuffle(neighbours)#randomises the order in which the neighbours will be resolved
            neighbour = neighbours[0]#gets the first neighbour
            if neighbour[0] - row == -1:#checking where the neighbour is relative to the current cell
                num1 = 0#sets the index num1 is for the current cell num2 is for neighbour cell, they must be opposite sides of the cell
                num2 = 2
            elif neighbour[1] - column == 1:
                num1 = 1
                num2 = 3
            elif neighbour[0] - row == 1:
                num1 = 2
                num2 = 0
            elif neighbour[1] - column == -1:
                num1 = 3
                num2 = 1

            maze[row][column][num1] = 1#sets the current cells open direction to allow access to neighbour
            maze[neighbour[0]][neighbour[1]][num2] = 1#sets neighbour cells open direciton to allow access to the current cell so you can go backwards

            maze[int(row)][int(column)][5] = True#the current cell has now been generated
            stackofcells.append([row,column])#adds the current cell to the stack 
            row = neighbour[0]#neighbour is the new current cell
            column = neighbour[1]

def get_moves(coords,maze):
    moves = []
    cell = maze[coords[0]][coords[1]]#assigns current cell
    directions = ["North","East","South","West"]
    for loop in range(4):#loops through the directions, if valid, adds them to a list of possible moves
        if cell[loop] == 1:
            moves.append(directions[loop])
    return moves

def player_move(coords,maze,start,finish):
    moves = get_moves(coords,maze)#gets possible moves
    message = "Which direction do you want to go:\n"#initializes message
    if start == True:#if the maze has just started then the appropiate message is made
        message = "You enter the dungeon, pick your direction: " + moves[0]
        start = False
    elif len(moves) == 1:#is it a dead end
        if coords == [0,0]:#are they back at the start
            message = "Your actually bad, you've made it all the way back to the start, where do you want to go: " + moves[0]
        elif coords == [finish[0],finish[1]]:#are they at the end
            message = "You made it! You found the exit to the maze, where do you want to go: " + moves[0] + " or exit. "
            moves.append("Exit") #add exit to the list of answers
        else:
            message = "You meet a dead end, which direction do you want to go, I dont think the decision will be hard: " + moves[0]
    else:#must be multiple options
        message += moves[0]#first direction has no comma
        for loop in range(1,len(moves)-1):#second has a comma
            message += ", " + moves[loop]
        message += " or " + moves[-1]#last direction has an 'or'
    message = txt.col.fg.nml.blue + message + "\n" + txt.sty.reset#adds colour
    answer = validate_input_from_array(moves,message)#asks for a valid direction input
    answer = answer.lower()

    end = False#default to dont end
    if answer == "north":#change location based on input
        coords[0] -= 1
    elif answer == "east":
        coords[1] += 1
    elif answer == "south":
        coords[0] += 1
    elif answer == "west":
        coords[1] -= 1
    elif answer == "exit":#if they exit, then return to exit
        end = True
    maze[int(coords[0])][int(coords[1])][4] = True
    return coords, maze, start, end

def display_dungeon(maze,coords,finish):
    whole_display = []#initializes entire display
    for row in range(len(maze)*2+1):#expands the maze by a factor of 2
        whole_display.append([])
        for column in range(len(maze[0])*2+1):
            whole_display[row].append("{}  {}".format(txt.col.bg.nml.red,txt.sty.reset))
    colour = "{}  {}".format(txt.col.bg.nml.blue,txt.sty.reset)#the colour for the walls

    for row in range(len(maze)):#loops through each row in the maze

        for column in range(len(maze[row])):#loops through each column in each row

            currentcell = maze[row][column]#assigns the current cell for ease
            display_coords = [row*2+1,column*2+1]#the corresponding coordinates of the currentcell in the display
            if currentcell[4] == True:
                for loop in range(-1,2):#sets the top left, top middle and middle left cells around the current cell to walls
                    for loop2 in range(-1,2):
                        whole_display[display_coords[0]+loop][display_coords[1]+loop2] = str(colour)
                if [row,column] == [finish[0],finish[1]]:#if the current cell is the end, make it green
                    person = "{}웃{}".format(txt.col.bg.nml.green,txt.sty.reset)
                    blank = "{}  {}".format(txt.col.bg.nml.green,txt.sty.reset)
                else:#otherwise make it plain
                    person = "웃"
                    blank = "  "
                if [row,column] == coords:#if the current cell is the player location, make it a person, otherwise make it empty
                    whole_display[display_coords[0]][display_coords[1]] = person
                else:
                    whole_display[display_coords[0]][display_coords[1]] = blank
                #if the current cell has an open direction to one of the neighbouring cells, change it to be empty, not a wall
                if currentcell[0] == 1:
                    whole_display[display_coords[0]-1][display_coords[1]] = "  "
                if currentcell[3] == 1:
                    whole_display[display_coords[0]][display_coords[1]-1] = "  "
                if currentcell[1] == 1:
                    whole_display[display_coords[0]][display_coords[1]+1] = "  "
                if currentcell[2] == 1:
                    whole_display[display_coords[0]+1][display_coords[1]] = "  "
    #fills in the bottom row and right column as walls, because of the way each cell only deals with its neighbours to the left and above, these 2 edges arent dealt with
    #for loop in range(len(whole_display)):
     #   whole_display[loop][-1] = str(colour)
    #for loop in range(len(whole_display[-1])):
     #   whole_display[-1][loop] = str(colour)
    print_display(whole_display)

def print_display(array):#prints the display
    for loop in array:
        for loop2 in loop:
            print(loop2,end="")
        print("")