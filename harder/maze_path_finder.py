"""

a = "\n".join([
  ".W.",
  ".W.",
  "..."
])


current = mazearray[0][0]

WIP!
"""


def path_finder(maze):
    mazearray = maze.split("\n")
    enumarray = []
    for i in mazearray:
        enumarray.append(list(enumerate(i)))
    visited = []
    queue = [enumarray[0][0]]
    end = enumarray[-1][-1]
    y = 0

    while queue:
        current = queue.pop(0)
        if current not in visited or current[0] not == 0 or enumarray[current[0]-1] not "W": : # if it is 0 then we know we have nothing to the left
            queue.push(enumarray[current[0]-1])
        if current not in visited or current[0] not == len(enumarray[0]) -1 or enumarray[current[0]+1] not "W": # if our current cell is not the last in this row...
            queue.push(enumarray[current[0]+1])
        if current not in visited or enumarray[y-1][current]
            
            
            
        current = 
