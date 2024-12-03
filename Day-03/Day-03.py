import re

def process_file(content):
    
    # Encontrar todas as ocorrências de mul("numero","numero")
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, content)
    
    results = 0
    for match in matches:
        num1, num2 = map(int, match)
        result = num1 * num2
        results = result + results
    
    return results


def process_file2(content):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, content)
    
    results = 0
    is_enabled = True

    for match in matches:
        if match == "do()":
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        else:
            if is_enabled:
                num1, num2 = map(int, re.findall(r"\d+", match))
                result = num1 * num2
                results = result + results        
    
    return results

with open("./Day-03/input.in") as file:
  input = file.read()

solution_1 = process_file(input)
solution_2 = process_file2(input)

print ("Answer to Day 03: \n Part 1 => ", solution_1, "\n Part 2 => ", solution_2)