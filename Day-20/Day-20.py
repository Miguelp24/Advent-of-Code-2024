from copy import deepcopy

def parse_data(my_file) -> tuple:
    with open(my_file) as f:
        maze = {}
        for y,line in enumerate(f.readlines()):
            for x, ch in enumerate(line.strip()):
                maze[y+x*1j] = ch
                if ch == 'S':
                    start = (y+x*1j)
                if ch == 'E':
                    end = (y+x*1j)
        return maze,start,end
def best_path(maze:dict, current: complex, end: complex) -> dict:
    visited = {current:0}
    while current != end:
        new = [n for d in [-1, 1, 1j, -1j] if maze[(n:=current+d)] != '#' and n not in visited][0]
        visited[new]=visited[current]+1
        current = new
    return visited
def find_cheats(track:dict, max_d:int = 20, max_save:int = 99) -> int:
    cheats = 0
    for k,v in list(track.items()):
        for k1,v1 in track.items():
            if 0<(cur_dist:=abs((d:=k1-k).real)+abs(d.imag))<=max_d:
                if abs(v1-v)-cur_dist>max_save:
                    cheats += 1
        del track[k]
    return cheats


data = parse_data('./Day-20/input.in')
track = best_path(*data)

solution_1 = find_cheats(deepcopy(track),2)
solution_2 = find_cheats(deepcopy(track),20)

print ("Answer to Day 20: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)