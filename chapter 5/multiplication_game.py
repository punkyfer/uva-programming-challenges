import math

winners = ["Stan", "Ollie"]

ranges = [0, math.log(9,18), 1]

def read_input():
    input_lines = []
    try:
        aux_line=int(input().strip())
        while aux_line != None:
            input_lines.append(aux_line)
            aux_line = int(input().strip())
    except EOFError:
        pass
    return input_lines

def calculate_winner(x):
    auxnum = math.log(x,18)
    if auxnum == 0: return 1
    auxnum = auxnum - math.floor(auxnum)
    if auxnum >= ranges[0] and auxnum <= ranges[1]:
        return 0
    elif auxnum > ranges[1] and auxnum <= ranges[2]:
        return 1

cases = read_input()

for case in cases:
    print (winners[calculate_winner(case)]+" wins.")