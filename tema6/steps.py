def read_input():
    cases = []
    try:
        aux_line = int(input().strip())
        for x in range(aux_line):
            aux_line = input().strip()
            cases.append([int(x) for x in aux_line.split(" ")])
    except EOFError:
        pass
    return cases

def difference_steps(difference):
    num_steps = 0
    if difference != 0:
        stepSum = 0
        z = 2
        while (difference>stepSum):
            stepSum += (z//2)
            num_steps += 1
            z += 1
    return num_steps

cases = read_input()
for case in cases:
    print (difference_steps(case[1]-case[0]))