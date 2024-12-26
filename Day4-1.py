def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    
    def check_word(r, c, dr, dc):
        if not (0 <= r + 3*dr < rows and 0 <= c + 3*dc < cols):
            return False
        return (grid[r][c] == 'X' and 
                grid[r+dr][c+dc] == 'M' and 
                grid[r+2*dr][c+2*dc] == 'A' and 
                grid[r+3*dr][c+3*dc] == 'S')
    
    def check_reverse(r, c, dr, dc):
        if not (0 <= r + 3*dr < rows and 0 <= c + 3*dc < cols):
            return False
        return (grid[r][c] == 'S' and 
                grid[r+dr][c+dc] == 'A' and 
                grid[r+2*dr][c+2*dc] == 'M' and 
                grid[r+3*dr][c+3*dc] == 'X')
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_word(r, c, dr, dc):
                    count += 1
                if check_reverse(r, c, dr, dc):
                    count += 1
                    
    return count

grid = [line.strip() for line in open('input.txt').readlines()]
print(f"XMAS appears {find_xmas(grid)} times")
