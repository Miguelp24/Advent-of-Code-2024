from collections import Counter

def calcular_distancia_total(lista_esquerda, lista_direita):
    # Ordenar as listas
    lista_esquerda.sort()
    lista_direita.sort()
    
    # Calcular a distância total
    distancia_total = 0
    for esq, dir in zip(lista_esquerda, lista_direita):
        distancia_total += abs(esq - dir)
    
    return distancia_total

def calcular_pontuacao_similaridade(lista_esquerda, lista_direita):
    # Contar a frequência de cada número na lista da direita
    contagem_direita = Counter(lista_direita)
    
    # Calcular a pontuação de similaridade
    pontuacao_similaridade = 0
    for numero in lista_esquerda:
        pontuacao_similaridade += numero * contagem_direita[numero]
    
    return pontuacao_similaridade

####
with open("./Day-01/input.in") as file:
    input_data = [line.split() for line in file.read().strip().split("\n")]

# Separar as listas esquerda e direita
lista_esquerda = [int(pair[0]) for pair in input_data]
lista_direita = [int(pair[1]) for pair in input_data]

solution_1 = calcular_distancia_total(lista_esquerda, lista_direita)
solution_2 = calcular_pontuacao_similaridade(lista_esquerda, lista_direita)

print("Answer to Day 01: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)