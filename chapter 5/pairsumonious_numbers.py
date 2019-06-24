def read_input():
    cases = []
    try:
        aux_line = input().strip()
        while (aux_line != None):
            split_line = aux_line.split(" ")
            cases.append([int(split_line[0])]+sorted([int(x) for x in split_line[1:]]))
            aux_line = input().strip()
    except EOFError:
        pass
    return cases

def solve_equations_3(case):
    c = (case[1] + case[2] - case[0]) / 2
    if not (c-int(c) == 0):
        return "Impossible"
    a = case[0] - case[2] + c
    b = case[2] - c
    if not (a-int(a)==0 and b-int(b)==0):
        return "Impossible"
    return [int(a),int(b),int(c)]

def add_new_variable(var_arr, case):
    d = case[0] - var_arr[0]
    if (d-int(d) != 0):
        return "Impossible", 'Impossible'
    for var in var_arr:
        
        if (d+var in case):
            case.remove(d+var)
        else:
            return "Impossible", 'Impossible'
    return d, case

def solve_equations(case, offset=0):
    num_vars = case[0]
    to_solve = sorted(case[1:])
    if offset >= num_vars-2:
        return "Impossible"
    else:
        var_arr = solve_equations_3([to_solve[0], to_solve[1], to_solve[2+offset]])
        if offset == 0:
            to_solve = to_solve[3:]
        else:
            to_solve = to_solve[2:2+offset] + to_solve[2+offset+1:]
    if var_arr == "Impossible":
        return solve_equations(case, offset+1)
    while len(var_arr) < case[0]:
        #print (to_solve)
        new_var, to_solve = add_new_variable(var_arr, to_solve)
        #print (new_var, to_solve)
        if new_var == "Impossible":
            return solve_equations(case, offset+1)
        var_arr += [new_var]

    return var_arr



cases = read_input()
for case in cases:
    solution = solve_equations(case, 0)
    if solution == "Impossible":
        print (solution)
    else:
        print (*solution)