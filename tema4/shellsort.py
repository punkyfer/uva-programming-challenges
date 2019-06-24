def read_input():
    cases = [[[],[]] for x in range(int(input()))]
    for case in cases:
        num_turtles = int(input())
        case[0] = [str(input()) for x in range(num_turtles)]
        case[1] = [str(input()) for x in range(num_turtles)]
    return cases

def calculate_move_order(to_move, desired_order):
    if len(to_move)>1:
        for elem in desired_order[::-1]:
            if elem in to_move:
                print (elem)
    else:
        for elem in to_move:
            print (elem)


def calculate_to_move(case):
    case_copy = [case[0][::-1], case[1][::-1]]
    to_move = []
    mod0 = 0
    for x in range(len(case_copy[1])):
        try:
            if case_copy[0][x+mod0] != case_copy[1][x]:
                while(case_copy[0][x+mod0] != case_copy[1][x]):
                    to_move.append(case_copy[0][x+mod0])
                    mod0+=1
        except IndexError:
            break
    return to_move

cases = read_input()

for case in cases:
    to_move = calculate_to_move(case)
    calculate_move_order(to_move, case[1])
    print()
    