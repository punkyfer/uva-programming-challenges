import bisect
import random

class BacktrackingScheme:
    def is_complete(self, s):
        # True if State s is complete
        return s[0] == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    
    def is_promising(self, s):
        # False if s does not contain any feasible solutions
        pass

    def heuristic(self, puzzle):
        if self.heuristic_mode == "man":
            return min_steps_req(puzzle)
        return count_inversions(puzzle)
    
    def branch(self, s):
        # Return states branched from s
        states = []
        #print(s, self.lastmove, s[3], s[s[3][0]+1][s[3][1]])
        # Up
        if (s[3][0] > 0 and s[2][-1] != "D"):
            np1 = [x[:] for x in s[0]]
            np1[s[3][0]][s[3][1]] = np1[s[3][0]-1][s[3][1]]
            np1[s[3][0]-1][s[3][1]] = 0
            states += [(np1, self.heuristic(np1)+len(s[2]), s[2]+"U", (s[3][0]-1, s[3][1]))]
        # Down
        if (s[3][0] < self.n and s[2][-1] != "U"):
            np2 = [x[:] for x in s[0]]
            np2[s[3][0]][s[3][1]] = np2[s[3][0]+1][s[3][1]]
            np2[s[3][0]+1][s[3][1]] = 0
            states += [(np2, self.heuristic(np2)+len(s[2]), s[2]+"D", (s[3][0]+1, s[3][1]))]
        # Left 
        if (s[3][1] > 0 and s[2][-1] != "R"):
            np3 = [x[:] for x in s[0]]
            np3[s[3][0]][s[3][1]] = np3[s[3][0]][s[3][1]-1]
            np3[s[3][0]][s[3][1]-1] = 0
            states += [(np3, self.heuristic(np3)+len(s[2]), s[2]+"L", (s[3][0], s[3][1]-1))]
        # Right
        if (s[3][1] < self.n and s[2][-1] != "L"):
            np4 = [x[:] for x in s[0]]
            np4[s[3][0]][s[3][1]] = np4[s[3][0]][s[3][1]+1]
            np4[s[3][0]][s[3][1]+1] = 0
            states += [(np4, self.heuristic(np4)+len(s[2]), s[2]+"R", (s[3][0], s[3][1]+1))]

        random.shuffle(states)
        return states
        
    def backtracking(self):
        # Returns first feasible solution or None
        """
        if self.is_complete(state):
            return True
        else:
            branches = self.branch(s)
            for i, sp in enumerate(branches):
                if (sp[1]  < min_dist):
                    min_dist = sp[1]
                    state = i
            self.lastmove = branches[state][2]
            self.blankpos = branches[state][3]
            self.moves += [branches[state][2]]
            print(branches[state])
            if(len(state[2]) >= 50):
                return False
            # I think now it only searches for 1 minimal path, but with the commented code below
            # i should be able to fix it so it searches the branch if its manhattan dist is <= current min md
            #for sp in self.branch(s):
            #if self.is_promising(sp):
            found = self.backtracking(branches[state][0])
            if found != False: return found
        return False
        """
        found = False
        while not found:
            if len(self.queue)==0:
                return False

            state = self.queue.pop(0)
            #print(state)
            if test_solvability(state[0], state[3]):
                if self.is_complete(state):
                    self.finalstate = state
                    found = True
                else:
                    branches = self.branch(state)
                    print(state)
                    print(branches)
                    for branch in branches:
                        if (branch[1]) < 50 and branch[1] <= state[1]:
                            self.queue.insert(bisect.bisect_left(self.keys, branch[1]), branch)
                            self.keys.insert(bisect.bisect_left(self.keys, branch[1]), branch[1])
                #self.queue = sorted(self.queue, key=lambda x: x[1], reverse=False)
        return found
    
    def __init__(self, s, blankpos):
        self.n = 3
        self.finalstate = None
        #self.queue = [[s, min_steps_req(s), "0", blankpos]]
        self.queue = [[s, count_inversions(s), "0", blankpos]]
        self.keys = [self.queue[0][1]]
        #self.heuristic_mode = "man"
        self.heuristic_mode = "cinv"

    def solve(self):
        if self.backtracking() != False:
            return ''.join(self.finalstate[2][1:])
        return "This puzzle is not solvable."

mh_dict = {}
def min_steps_req(puzzle):
    try:
        return mh_dict[str(puzzle)]
    except KeyError:
        pass
    prow = row = [x for y in puzzle for x in y]
    irow = [(3,3), (0,0), (0,1), (0,2), (0,3), (1,0), (1,1), 
    (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1),
    (3,2)]
    mh_dist = 0
    for row, prow in enumerate(puzzle):
        for col, elem in enumerate(prow):
            mh_dist += abs(irow[elem][0]-row) + abs(irow[elem][1] - col)

    mh_dict[str(puzzle)] = mh_dist
    return mh_dist


def count_inversions(puzzle):
    num_inv = 0
    row = [x for y in puzzle for x in y]
    for i, num in enumerate(row[:-1]):
        if num != 0:
            for nextnum in row[i+1:]:
                if nextnum != 0:
                    if nextnum < num:
                        num_inv+=1
    return num_inv
                    
def test_solvability(puzzle, blankpos):
    num_inv = count_inversions(puzzle)
    num_row = (3 - blankpos[0]) + 1
    return (num_inv % 2 == 0) == (num_row % 2 != 0)


def read_input():
    cases = []
    try:
        num_cases = int(input().strip())
        for x in range(num_cases):
            zeroPos = None
            puzzle=[]
            for y in range(4):
                aux_line = [int(x) for x in input().strip().split(" ")]
                if 0 in aux_line:
                    zeroPos = (y,aux_line.index(0))
                puzzle.append(aux_line)
            cases.append((puzzle, zeroPos))
    except EOFError:
        pass
    return cases

puzzles = read_input()

for puzzle in puzzles:
    if test_solvability(puzzle[0], puzzle[1]):
        if min_steps_req(puzzle[0]) < 50:
            br_scheme = BacktrackingScheme(puzzle[0], puzzle[1])
            print (br_scheme.solve())
        else:
            print ("This puzzle is not solvable.")
    else:
        print ("This puzzle is not solvable.")