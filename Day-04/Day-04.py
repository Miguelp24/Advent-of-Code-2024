def count_xmas(grid):
    def search(x, y, dx, dy):
        # Verifica se XMAS está na direção especificada
        for i in range(4):
            if grid[y + dy * i][x + dx * i] != "XMAS"[i]:
                return False
        return True

    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0)]
    
    for y in range(rows):
        for x in range(cols):
            for dx, dy in directions:
                if 0 <= x + dx * 3 < cols and 0 <= y + dy * 3 < rows:
                    if search(x, y, dx, dy):
                        count += 1
    return count

def count_xmas_part2(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(1, rows):
        for j in range(1, cols):
            # Encontra "A" no centro de um bloco 3x3
            if grid[i][j] == "A" and i < rows - 1 and j < cols - 1:
                # Verifica os cantos para ambos os casos.
                if grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S":
                    if grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S":
                        count += 1
                    elif grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M":
                        count += 1
                elif grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M":
                    if grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S":
                        count += 1
                    elif grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M":
                        count += 1

    return count


with open("./Day-04/input.in") as file:
    input_grid = [line.strip() for line in file.readlines()]

solution_1 = count_xmas(input_grid)
solution_2 = count_xmas_part2(input_grid)

print("Answer to Day 04: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)
