def read_input():
    cases = []
    try:
        aux_line = input().strip()
        while (aux_line != None):
            cases.append(int(aux_line))
            aux_line = input().strip()
    except EOFError:
        pass
    return cases

def find_ones(num):
    calc_array = [1%num]
    for x in range(1,num+1):
        if calc_array[-1]==0:
            return len(calc_array)
        else:
            calc_array.append((calc_array[-1]*10+1)%num)

cases = read_input()

for case in cases:
    print (find_ones(case))