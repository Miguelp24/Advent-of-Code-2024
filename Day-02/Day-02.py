#Parte 1

def seguro(levels):
  crescente = all(levels[i] < levels[i+1] for i in range(len(levels)-1))
  decrescente = all(levels[i] > levels[i+1] for i in range(len(levels)-1))

  if not (crescente or decrescente):
    return False
  
  for i in range(len(levels)-1):
    if abs(levels[i] - levels[i+1]) < 1 or abs(levels[i] - levels[i+1]) > 3:
      return False
    
  return True

def contar(reports):
  count = 0
  for report in reports:
    levels = list(map(int, report.split()))
    if seguro(levels):
      count += 1

  return count  

#Parte 2
def seguro_damper(levels):
  #Se é seguro sem remover nenhum nivel
  if seguro(levels):
    return True
  
  #Se é seguro removendo um nivel
  for i in range(len(levels)):
    new_levels = levels[:i] + levels[i+1:]
    if seguro(new_levels):
      return True
    
  return False


def contar_damper(reports):
  count = 0
  for report in reports:
    levels = list(map(int, report.split()))
    if seguro_damper(levels):
      count += 1

  return count


####
with open("./Day-02/input.in") as file:
  input = [i for i in file.read().strip().split("\n")]

solution_1 = contar(input)
solution_2 = contar_damper(input)

print ("Answer to Day 02: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)