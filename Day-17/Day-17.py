import re
from sys import argv

def program(prog, A):
    B = 0
    C = 0
    outputs = []

    def combo(i):
        c = [0, 1, 2, 3, A, B, C]
        return c[i]

    ip = 0
    while ip < len(prog):
        op = prog[ip]
        val = prog[ip+1]
        if op == 0:
            A = A >> combo(val)
        elif op == 1:
            B = B ^ val
        elif op == 2:
            B = combo(val) % 8
        elif op == 3:
            if A != 0:
                ip = val - 2
        elif op == 4:
            B = B ^ C
        elif op == 5:
            outputs.append(combo(val) % 8)
        elif op == 6:
            B = A >> combo(val)
        elif op == 7:
            C = A >> combo(val)
        ip += 2
    return outputs

def recurse(prog, A, i):
    for k in range(8):
        z = k << 3 * i
        if A + z == 0: continue  # Ignora caso A+z seja 0
        result = program(prog, A + z)
        if result[i] == prog[i]:  # Compara a saída com o programa
            if i == 0:
                return z
            if (lower := recurse(prog, A + z, i - 1)) >= 0:
                return z + lower
    return -1

if __name__ == "__main__":
    with open("./Day-17/input.in") as f:
        # Lê os valores de A, B, C e o programa do arquivo
        A = int(re.search(r"A: (\d+)", f.readline())[1])
        B = int(re.search(r"B: (\d+)", f.readline())[1])
        C = int(re.search(r"C: (\d+)", f.readline())[1])
        f.readline()  # Ignora a linha em branco
        prog = [int(c) for c in re.search(r"Program: ((?:\d+,?)+)", f.readline())[1].split(",")]

    print(f"Part 1 => {program(prog, A)}")

    result = recurse(prog, 0, 15)  # Tenta encontrar o valor correto de A
    if result >= 0:
        print(f"Part 2 => {result}")
    else:
        print("Nenhum valor válido encontrado para A.")
