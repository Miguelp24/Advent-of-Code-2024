def calculate_trailhead_scores(topography):
    rows = len(topography)
    cols = len(topography[0])
    
    # Função para verificar se uma posição está dentro do mapa e pode ser visitada
    def is_valid(x, y, current_height, local_visited):
        return (
            0 <= x < rows and
            0 <= y < cols and
            not local_visited[x][y] and
            topography[x][y] == current_height + 1
        )
  
    def dfs(x, y):
        stack = [(x, y)]
        local_visited = [[False] * cols for _ in range(rows)]
        reachable_nines = set()
        
        while stack:
            cx, cy = stack.pop()
            local_visited[cx][cy] = True
            if topography[cx][cy] == 9:
                reachable_nines.add((cx, cy))
            
            # Movimentos possíveis: cima, baixo, esquerda, direita
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, topography[cx][cy], local_visited):
                    stack.append((nx, ny))
        
        return len(reachable_nines)
    
    total_score = 0
    
    for r in range(rows):
        for c in range(cols):
            if topography[r][c] == 0:
                total_score += dfs(r, c)
    
    return total_score

#part 2

def calculate_trailhead_ranks(topography):
    rows = len(topography)
    cols = len(topography[0])
    
    # Função para verificar se uma posição está dentro do mapa e pode ser visitada
    def is_valid(x, y, current_height, visited):
        return (
            0 <= x < rows and
            0 <= y < cols and
            not visited[x][y] and
            topography[x][y] == current_height + 1
        )
    
    # Realiza a busca em profundidade para contar trilhas distintas
    def dfs_count_paths(x, y, visited):
        if topography[x][y] == 9:
            return 1  # Encontramos um destino final válido
        
        visited[x][y] = True
        total_paths = 0
        
        # Movimentos possíveis: cima, baixo, esquerda, direita
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, topography[x][y], visited):
                total_paths += dfs_count_paths(nx, ny, visited)
        
        visited[x][y] = False  # Voltar para explorar outras trilhas
        return total_paths
    
    total_rank = 0
    
    for r in range(rows):
        for c in range(cols):
            if topography[r][c] == 0:
                # Inicializa uma matriz de visitados para cada trilha
                visited = [[False] * cols for _ in range(rows)]
                # Calcula o número de trilhas distintas para o início atual
                total_rank += dfs_count_paths(r, c, visited)
    
    return total_rank

with open("./Day-10/input.in") as file:
    input = [[int(char) for char in line] for line in file.read().strip().split("\n")]

solution_1 = calculate_trailhead_scores(input)
solution_2 = calculate_trailhead_ranks(input)

print("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)

