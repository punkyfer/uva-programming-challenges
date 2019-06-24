
aux_line = input()
cycle_dict = {1:[1]}


def calculate_cycle(x):
    cycle = [x]
    while x != 1:
        if x in cycle_dict.keys():
            return cycle + cycle_dict[x]
        if x%2 == 0:
            x = x/2
            cycle.append(x)
        else:
            x = (3*x)+1
            cycle.append(x)
    return cycle

while aux_line:
    nums = aux_line.strip().split(" ")

    i, j = int(nums[0]), int(nums[1])
    if i>j:
        top, bottom = i+1, j
    else:
        top, bottom = j+1, i
    max_length = 0
    for x in range(bottom, top):
        if x not in cycle_dict.keys():
            cycle_dict[x] = calculate_cycle(x)
        cycle_length = len(cycle_dict[x])
        if cycle_length > max_length:
            max_length = cycle_length
            
    print (str(i)+" "+str(j)+" "+str(max_length))
    
    try:
        aux_line = input()
    except EOFError:
        aux_line=None



