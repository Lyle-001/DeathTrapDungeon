#this program is completely for test purposes to run the dungeon maze
#the ONLY INPUTS NEEDED to run the maze are the number of row and columns

import dungeon_maze
import ansi_codes
rows = int(input("rows"))
columns = int(input("columns"))
maze,finish,coords = dungeon_maze.generate_maze(rows,columns)
start = True
ansi_codes.clearscreen()
end = False
while end == False:
    dungeon_maze.display_dungeon(maze,coords,finish)
    coords,maze,start,end = dungeon_maze.player_move(coords,maze,start,finish)
    ansi_codes.clearscreen()