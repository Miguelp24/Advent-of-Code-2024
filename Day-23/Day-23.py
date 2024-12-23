graph = {}

with open("./Day-23/input.in") as file:
    for line in file:
        nodes = line.rstrip().split("-")
        for node in nodes:
            if node not in graph:
                graph[node] = []
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])

max_lan_size = -1
lan_parties_with_t = 0
def check_lan(node_list, lan_list, idx):
    global max_lan_size, lan_parties_with_t
    for i in range(idx,len(node_list)):
        node = node_list[i]
        if node in explored_set:
            continue
        if not all(node in graph[n] for n in lan_list):
            continue
        lan_list.append(node)
        check_lan(node_list, lan_list, i+1)
        if len(lan_list) == 3 and any(n[0] == 't' for n in lan_list):
            lan_parties_with_t += 1
        if len(lan_list) > max_lan_size:
            max_lan_size = len(lan_list)
            print(f"Found bigger lan size {max_lan_size}: {','.join(x for x in sorted(lan_list))}")
        lan_list.remove(node)

explored_set = set()
for node in graph:
    check_lan(graph[node], [node], 0)
    explored_set.add(node)


with open("./Day-23/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

solution_1 = lan_parties_with_t
solution_2 = 0

print ("Answer to Day 23: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)