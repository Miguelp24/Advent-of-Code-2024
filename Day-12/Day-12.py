grid = open("./Day-12/input.in").read().splitlines()
xn, yn = len(grid), len(grid[0])

def neighbours(x, y):
    return {(x+dx, y+dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]}
    
def neighbours_in_same_region(x, y):
    return {(x1, y1) for x1, y1 in neighbours(x, y) 
            if 0<=x1<xn and 0<=y1<yn and grid[x][y]==grid[x1][y1]}

def count_corners(x, y, region):
    return sum(((x, y+dy) not in region and (x+dx, y) not in region) or 
               ((x, y+dy) in region and (x+dx, y) in region and (x+dx, y+dy) not in region)
               for dx in (1,-1) for dy in (1,-1))

solution_2 = solution_1 = 0
remaining_plots = {(x,y) for x in range(xn) for y in range(yn)} 

while remaining_plots:
    region = set()
    frontier = {remaining_plots.pop()}
    while frontier:
        region.add(plot:=frontier.pop())
        new_frontier = neighbours_in_same_region(*plot) & remaining_plots
        frontier |= new_frontier
        remaining_plots -= new_frontier
    solution_1 += len(region)*sum(len(neighbours(*plot)-region) for plot in region)
    solution_2 += len(region)*sum(count_corners(*plot, region) for plot in region)


print("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)