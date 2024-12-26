# Define markers representing directions in the maze
marker = ['^', '>', 'v', '<']  # Up, Right, Down, Left
# Define the obstacle character in the maze
obstacle = '#'
# Initialize a global variable to store the result value
resultVal = 0

# Create a dictionary to define movements corresponding to each direction
directions = {
    '^': (-1, 0),  # Move Up: Decrease row index by 1
    '>': (0, 1),  # Move Right: Increase column index by 1
    'v': (1, 0),  # Move Down: Increase row index by 1
    '<': (0, -1)  # Move Left: Decrease column index by 1
}


# Function to find the starting position and direction in the maze
def startingPoint(maze, rows, cols):
    for i in range(rows):  # Iterate through every row
        for j in range(cols):  # Iterate through every column
            # If a cell contains one of the directional markers, return it
            if maze[i][j] in marker:
                return maze[i][j], i, j
            else:
                continue  # Otherwise, skip to the next cell


# Function to turn the current direction to the right
def turnRight(direction):
    for i in range(len(marker)):  # Loop through the list of possible directions
        if direction == marker[i]:  # Find the current direction
            # Update to the next direction in the list, or wrap around if at the end
            direction = marker[i + 1] if i != 3 else marker[0]
            break
    return direction


# Functions to calculate new positions based on direction
def Up(row, col):
    # Move up unless already at the top row
    if row != 0:
        row -= 1
    return row, col


def Down(row, col):
    # Move down unless already at the bottom row
    if row != gridRow:
        row += 1
    return row, col


def Right(row, col):
    # Move right unless already at the last column
    if col != gridCol:
        col += 1
    return row, col


def Left(row, col):
    # Move left unless already at the first column
    if col != 0:
        col -= 1
    return row, col


# Function to create a tuple representing the new point (row, col)
def updatePoint(row, col):
    pointArr = (row, col)
    return pointArr


# Function to move along the maze and explore all reachable spots
def move(direction, row, col):
    global resultVal
    # Initialize variables to track the current position
    checkRow, checkCol = row, col
    while True:  # Infinite loop to continue exploring the maze
        # Calculate the direction offset for row and column
        dr, dc = directions[direction]
        # Update the position to the next cell
        checkRow, checkCol = checkRow + dr, checkCol + dc
        # Check if the move is out of bounds
        if not (0 <= checkRow < gridRow) and (0 <= checkCol < gridCol):
            break  # Break the loop if the move is invalid
        # Check if an obstacle is encountered
        if input_data[checkRow][checkCol] == obstacle:
            # Turn right to change direction
            direction = turnRight(direction)
            # Reset position to the last valid cell
            checkRow, checkCol = row, col
        else:
            # Update the position based on the current direction
            row, col = moveMarker[direction](row, col)
            # Mark the updated position as visited
            visited.add(updatePoint(row, col))


# Function to calculate the dimensions of the maze
def maze_length(maze):
    maze_row = len(maze)  # Number of rows
    maze_col = len(maze[0])  # Number of columns in the first row
    return maze_row, maze_col


# Read the maze input from a file
with open("../input_day6.txt", "r") as file:
    input_data = file.readlines()

# Map each direction to its corresponding movement function
moveMarker = {'^': Up, '>': Right, 'v': Down, '<': Left}

# Calculate the dimensions of the maze (rows and columns)
gridRow, gridCol = maze_length(input_data)

# Determine the starting direction and position in the maze
direction, startRow, startCol = startingPoint(input_data, gridRow, gridCol)

# Create a starting point tuple (row, column)
startPoint = (startRow, startCol)

# Create a set to store visited positions and add the starting point to it
visited = set()
visited.add(startPoint)

# Begin exploring the maze
move(direction, startRow, startCol)

# Print the total number of unique visited cells
print(len(visited))
