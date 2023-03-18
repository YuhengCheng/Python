#import functions from maze helper
from maze_helper import sample_maze, get_adjacent_positions, symbol_at, add_walk_symbol, print_maze

#define the path finder function
def dfs(maze, position, explored=[]):
   #append the current position
    explored.append(position)
    #get adjacent positions
    adjacent_pos = get_adjacent_positions(maze,position)
    #check all possibilties
    for i in range(len(adjacent_pos)):
        #see if the end is adjacent
        if symbol_at(maze,adjacent_pos[i])=='X':
                #mark the path
                for i in range(len(explored)):
                    add_walk_symbol(maze,explored[i])
                pass
        #continue the path
        elif adjacent_pos[i] not in explored:
            dfs(maze, adjacent_pos[i])



   
    #return the maze
    return maze

#define main 
def main():
    #look for the starting point
    for i in range(len(sample_maze())):
        for j in range(len(sample_maze()[i])):
            if symbol_at(sample_maze(),(i,j)) == "O":
                #call search function with  starting point as current pos
                path = dfs(sample_maze(),(i,j))
                #print the maze
                print_maze(path)

#call main
if __name__ == "__main__":
    main()







