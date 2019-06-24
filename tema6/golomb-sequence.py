def read_input():
    cases = []
    try:
        aux_line = input().strip()
        while (aux_line != None):
            cases.append(int(aux_line))
            aux_line = input().strip()
            if int(aux_line) == 0:
                break
    except EOFError:
        pass
    return cases

def pre_generate():
    golomb_table = [0]
    golomb_table.append(1)   # [1] = 1
    golomb_table.append(3)   # [2] = 3
    golomb_table.append(5)   # [3] = 5
    golomb_table.append(8)   # [4] = 8
    golomb_table.append(11) # [5] = 11
    golomb_table.append(15) # [6] = 15
    
    n = 7
    while (golomb_table[-1] <= 2000000000):
        golomb_table.append(golomb_table[-1]+binary_search(golomb_table, n, 1, len(golomb_table)-1))
        n+=1
        
    return golomb_table

def binary_search(numbers, x, low, hi):
    ans = -1
    if low==hi: ans = -1
    else:
        mid = (low+((hi-low)//2))
        if x < numbers[mid]:
            if x > numbers[mid-1]: ans = mid
            else: ans = binary_search(numbers, x, low, mid)
        elif x > numbers[mid]: ans = binary_search(numbers, x, mid+1, hi)
        else: ans = mid
    return ans

cases = read_input()

golomb_table = pre_generate()

for elem in golomb_table:
    print ("golomb_table.append("+str(elem)+")")

"""
for case in cases:
    print (binary_search(golomb_table, case, 1, len(golomb_table)-1))
"""