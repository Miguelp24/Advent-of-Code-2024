def ler_regras(regras):
    regras_list = []
    for linha in regras:
        x, y = map(int, linha.split('|'))
        regras_list.append((x, y))
    return regras_list

def ler_atualizacoes(atualizacoes):
    atualizacoes_list = []
    for linha in atualizacoes:
        atualizacoes_list.append(list(map(int, linha.split(','))))
    return atualizacoes_list

def ordem_correta(regras, atualizacao):
    for x, y in regras:
        if x in atualizacao and y in atualizacao:
            if atualizacao.index(x) > atualizacao.index(y):
                return False
    return True

def ordenar_atualizacao(regras, atualizacao):
    from collections import defaultdict, deque

    grafo = defaultdict(list)
    grau = defaultdict(int)

    for x, y in regras:
        if x in atualizacao and y in atualizacao:
            grafo[x].append(y)
            grau[y] += 1

    fila = deque([n for n in atualizacao if grau[n] == 0])
    resultado = []

    while fila:
        no = fila.popleft()
        resultado.append(no)
        for vizinho in grafo[no]:
            grau[vizinho] -= 1
            if grau[vizinho] == 0:
                fila.append(vizinho)

    return resultado

def numero_pagina_meio(atualizacao):
    return atualizacao[len(atualizacao) // 2]

def calcular_soma_paginas_meio(regras, atualizacoes):
    soma_meio = 0
    for atualizacao in atualizacoes:
        if ordem_correta(regras, atualizacao):
            soma_meio += numero_pagina_meio(atualizacao)
    return soma_meio

def calcular_soma_paginas_meio_ordenadas_incorretas(regras, atualizacoes):
    soma_meio = 0
    for atualizacao in atualizacoes:
        if not ordem_correta(regras, atualizacao):
            atualizacao_corrigida = ordenar_atualizacao(regras, atualizacao)
            soma_meio += numero_pagina_meio(atualizacao_corrigida)
    return soma_meio

with open("./Day-05/input.in") as file:
    input_data = [linha for linha in file.read().strip().split("\n")]

# Separar regras e atualizações
indice_vazio = input_data.index('')
regras = ler_regras(input_data[:indice_vazio])
atualizacoes = ler_atualizacoes(input_data[indice_vazio + 1:])

solution_1 = calcular_soma_paginas_meio(regras, atualizacoes)
solution_2 = calcular_soma_paginas_meio_ordenadas_incorretas(regras, atualizacoes)

print("Answer to Day 05: \n Part 1 =>", solution_1, "\n Part 2 =>", solution_2)

