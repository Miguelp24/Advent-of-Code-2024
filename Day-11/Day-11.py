from collections import Counter


def evoluir_pedras(arranjo_inicial, piscares):
    # Conta as ocorrências de cada pedra inicialmente
    pedras = Counter(arranjo_inicial)
    
    for _ in range(piscares):
        novo_estado = Counter()
        for pedra, quantidade in pedras.items():
            if pedra == 0:
                # Regra 1: Pedra com 0 vira 1
                novo_estado[1] += quantidade
            elif len(str(pedra)) % 2 == 0:
                # Regra 2: Pedra com número par de dígitos se divide em duas
                meio = len(str(pedra)) // 2
                esquerda = int(str(pedra)[:meio])
                direita = int(str(pedra)[meio:])
                novo_estado[esquerda] += quantidade
                novo_estado[direita] += quantidade
            else:
                # Regra 3: Multiplicar o número por 2024
                novo_estado[pedra * 2024] += quantidade
        pedras = novo_estado
    
    # Retorna o total de pedras
    return sum(pedras.values())

with open("./Day-11/input.in") as file:
  input = [int(i) for i in file.read().strip().split()]


solution_1 = evoluir_pedras(input, 25)
solution_2 = evoluir_pedras(input, 75)

print("Answer to Day 11: \n Part 1 =>", solution_1, "\n Part 2 =>", solution_2)
