def read_input():
    cases = []
    try:
        aux_line = int(input().strip())
        for case in range(aux_line):
            istate = input().strip()
            while istate == "": istate = input().strip()
            initial_state = [int(j) for j in istate.split()]
            target_state = [int(j) for j in input().strip().split()]
            forbidden_states = []
            num_f_states = int(input().strip())
            for fcase in range(num_f_states):
                f_state = tuple([int(j) for j in input().strip().split()])
                forbidden_states += [f_state]

            cases += [[tuple(initial_state), tuple(target_state), forbidden_states]]
    except EOFError:
        pass
    return cases

class BFSScheme:

    def branch(self, s):
        states = []
        slist = list(s)
        listlen = len(slist)
        for i, num in enumerate(slist):
            if num == 9:
                newstate = slist[0:i] + [0] + slist[i+1:listlen]
                states.append(tuple(newstate))
            else:
                newstate = slist[0:i] + [num+1] + slist[i+1:listlen]
                states.append(tuple(newstate))

            if num == 0:
                newstate = slist[0:i] + [9] + slist[i+1:listlen]
                states.append(tuple(newstate))
            else:
                newstate = slist[0:i] + [num-1] + slist[i+1:listlen]
                states.append(tuple(newstate))

        return states
        
    def BFS(self):
        while self.state_queue:
            state = self.state_queue.pop(0)
            if state == self.target_state:
                return True
            for branch in self.branch(state):
                if branch not in self.visited_states:
                    self.state_depth[branch] = self.state_depth[state] + 1
                    self.visited_states.add(branch)
                    self.state_queue.append(branch)
        return False
    
    def __init__(self, initial_state, target_state, forbidden_states):
        self.initial_state = initial_state
        self.target_state = target_state
        self.forbidden_states = forbidden_states
        self.visited_states = set([initial_state])
        self.state_depth = {}
        self.state_depth[initial_state] = 0
        for st in forbidden_states:
            self.visited_states.add(st)
        self.state_queue = [initial_state]

        
    def solve(self):
        if self.target_state == self.initial_state:
            return 0
        if self.target_state in self.forbidden_states:
            return -1
        if self.BFS() != False:
            return self.state_depth[self.target_state]
        return -1


cases = read_input()
for case in cases:
    bfs = BFSScheme(case[0], case[1], case[2])
    print(bfs.solve())