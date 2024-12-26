turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
# Define the obstacle character in the maze
obstacle = '#'
# Create a dictionary to define movements corresponding to each direction
directions = {
    '^': (-1, 0),  # Move Up: Decrease row index by 1
    '>': (0, 1),  # Move Right: Increase column index by 1
    'v': (1, 0),  # Move Down: Increase row index by 1
    '<': (0, -1)  # Move Left: Decrease column index by 1
}

def simulateObstruction(input_data,obstructionVar,startpos,startDir):
    maze = [list(rows) for rows in input_data]
    row,col = obstructionVar
    maze[row][col] = obstacle

    position = (startpos)
    direction = startDir
    visited  = set()

    while True:
        state = (position,direction)
        if state in visited:
            return True

        visited.add(state)

        dr,dc = directions[direction]
        nextPos = (position[0]+dr,position[1]+dc)
        if not ((0<=nextPos[0]<gridRow) and (0<=nextPos[1]<gridCol)):
            return False
        if maze[nextPos[0]][nextPos[1]] == obstacle:
            direction = turn_right[direction]
            nextPos = position
        else:
            position = nextPos
    maze[row][col] = '.'

with open("../input_day6.txt", "r") as file:
  input_data = file.readlines()

gridRow,gridCol = len(input_data),len(input_data[0])
valid_positions = set()
startPos, startDir = None, None

for i in range(gridRow):
  for j in range(gridCol):
      if input_data[i][j] in '<>^v':
          startPos = (i,j)
          startDir = input_data[i][j]
      elif input_data[i][j] == ".":
          valid_positions.add((i,j))
      else:continue
print(startPos,startDir)
loop_positons = set()
print(len(valid_positions))
for obstacles in valid_positions:
    if simulateObstruction(input_data,obstacles,startPos,startDir):
        loop_positons.add(obstacles)
        print(len(loop_positons))

