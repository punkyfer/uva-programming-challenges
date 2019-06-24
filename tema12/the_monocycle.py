class Graph:
  # Directions
  # - North = 1
  # - East = 2
  # - South = 3
  # - West = 4
  
  # Wheel Colors
  # - Green = 1
  # - Black = 2
  # - Red = 3
  # - Blue = 4
  # - White = 5

  def __init__(self, rows, cols, matrix):
    self.nrows = rows - 1
    self.ncols = cols - 1
    self.matrix = matrix
    self.start_pos, self.end_pos = self.find_start_end()
    self.start_state = (self.start_pos[0], self.start_pos[1], 1, 1)

  def get_next_color(self, color):
    if color == 5:
      return 1
    else:
      return color+1

  def branch(self, state):
    branches = []
    # Turn Left or Right (+1 or -1 Directions)
    if state[2] == 4:
      new_state1 = (state[0], state[1], 1, state[3])
      new_state2 = (state[0], state[1], 3, state[3])
    elif state[2] == 1:
      new_state1 = (state[0], state[1], 2, state[3])
      new_state2 = (state[0], state[1], 4, state[3])
    else:
      new_state1 = (state[0], state[1], state[2]-1, state[3])
      new_state2 = (state[0], state[1], state[2]+1, state[3])

    branches += [new_state1, new_state2]

    # Move forward
    if state[2]==1:
      if state[0] == 0: return branches
      if self.matrix[state[0]-1][state[1]] == "#": return branches
      new_state3 = (state[0]-1, state[1], 1, self.get_next_color(state[3]))
    if state[2]==3:
      if state[0] == self.nrows: return branches
      if self.matrix[state[0]+1][state[1]] == "#": return branches
      new_state3 = (state[0]+1, state[1], 3, self.get_next_color(state[3]))
    if state[2]==4: 
      if state[1] == 0: return branches
      if self.matrix[state[0]][state[1]-1] == "#": return branches
      new_state3 = (state[0], state[1]-1, 4, self.get_next_color(state[3]))
    if state[2]==2: 
      if state[1] == self.ncols: return branches
      if self.matrix[state[0]][state[1]+1] == "#": return branches
      new_state3 = (state[0], state[1]+1, 2, self.get_next_color(state[3]))

    branches += [new_state3]

    return branches

  def is_final_state(self, state):
    return (state[0] == self.end_pos[0] and state[1] == self.end_pos[1] and state[3] == 1)

  def bfs(self):
    seen = {}
    cost = {self.start_state:0}
    queue = [self.start_state]
    found = False
    final_state = 0
    while queue:
      node = queue.pop(0)
      try:
        seen[node]
      except:
        seen[node]=True
        if self.is_final_state(node):
          found = True
          final_state = node
          break
        branches = self.branch(node)
        for branch in branches:
          cost[branch] = cost[node] + 1
          queue+=[branch]

    if not found:
      return False
    else:
      return cost[final_state]



  def find_start_end(self):
    start = []
    end = []
    for i, row in enumerate(self.matrix):
      if 'S' in row:
        start = [i, row.index('S')]
      if 'T' in row:
        end = [i, row.index('T')]

    return start, end

def read_input():
  cases = []
  while (True):
    m, n = (int(x) for x in input().split())
    matrix = []
    if m==0 and n==0:
      break
    for i in range(m):
      matrix += [input()]
    cases += [Graph(m,n,matrix)]

  return cases

cases = read_input()
for i, case in enumerate(cases):
  print ("Case #{}".format(i+1))
  min_steps = case.bfs()
  if not min_steps:
    print ("destination not reachable")
  else:
    print ("minimum time = {} sec".format(min_steps))

  if i+1 != len(cases):
    print ()