

bytes_in = [tuple(map(int, l.strip().split(","))) for l in open("./Day-18/input.in").readlines()]
sz = max(bytes_in)[0]

def adjs(xy):
    (x, y) = xy
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def is_ok(obstacles, xy):
    (x, y) = xy
    return not xy in obstacles and 0 <= x <= sz and 0 <= y <= sz

def bfs(obstacles, dist, layers):
    while edge := set(nxy for xy in layers[-1] 
                          for nxy in adjs(xy) if is_ok(obstacles, nxy) and nxy not in dist):
        dist.update({ xy: len(layers) for xy in edge })
        layers += [edge]

    return dist

def distance(obstacles, start = (0,0), end = (sz, sz)):
    return bfs(set(obstacles), { start: 0 }, [{start}]).get(end, 9999)



solution_1 = distance(bytes_in[:1024])
solution_2 = next(bytes_in[:i][-1] for i in range(len(bytes_in)) if distance(bytes_in[:i]) == 9999)

print ("Answer to Day 18: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)