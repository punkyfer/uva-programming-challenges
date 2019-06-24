import math

def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        while aux_line == "":
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          return cases

        town_array = [[0 for x in range(num_towns)] for y in range(num_towns)]
        
        for x in range(num_town_pairs):
          town1, town2, capacity = (int(x) for x in input().strip().split(" ") if x!="")
          town_array[town1-1][town2-1] = capacity
          town_array[town2-1][town1-1] = capacity
        start_city, end_city, num_tourists = (int(x) for x in input().strip().split(" ") if x!="")

        cases.append((town_array, start_city, end_city, num_tourists))

    except EOFError:
      pass


class BranchAndBoundTourists:

  def __init__(self, graph, start, end):
    self.graph = graph
    self.num_towns = len(graph)
    self.start = start
    self.end = end
    self.R = {}

  def is_complete(self, q):
    return q[0]==self.start and q[-1]==self.end

  def path_cost(self, path):
    if len(path)==1: return 0
    else:
      min_sol = 1000000
      for i,x in enumerate(path[:-1]):
        if self.graph[x-1][path[i+1]-1] < min_sol:
          min_sol = self.graph[x-1][path[i+1]-1]
      return min_sol

  def memoized_path_cost(self, path):
    if len(path)==1: self.R[str(path)] = 0
    else:
      if str(path) not in self.R:
        if self.R[str(path[:-1])] != 0:
          self.R[str(path)] = min(self.memoized_path_cost(path[:-1]),self.graph[path[-2]-1][path[-1]-1])
        else:
          self.R[str(path)] = self.graph[path[-2]-1][path[-1]-1]
    return self.R[str(path)]

  def branch(self, s):
    branches = []
    temp_array = [0 for x in range(self.num_towns)]
    num_row = self.graph[s[-1]-1]
    for i,x in enumerate(num_row):
      if x!=0: 
        if i+1 not in s:
          branches.append((s+[i+1], self.path_cost(s+[i+1])))
    return branches

  def branch_and_bound(self):
    active_set = [[self.start]]
    bestval = 0
    currentbest = None
    while len(active_set)!=0:
      node = active_set.pop(0)
      node_weight = self.path_cost(node)

      children_w = self.branch(node)
      for children, weight in children_w:
        if weight < bestval: pass
        elif self.is_complete(children):
          bestval, currentbest = weight, children
        else: 
          if weight<=node_weight:
            active_set.append(children)
          else:
            node_weight = weight
            active_set.insert(0, children)
          
    return bestval, currentbest

puzzles = read_input()


for c,puzzle_arr in enumerate(puzzles):
  puzzle = puzzle_arr[0]
  start_city, end_city = puzzle_arr[1], puzzle_arr[2]
  num_tourists = puzzle_arr[3]

  bbtourists = BranchAndBoundTourists(puzzle, start_city, end_city)
  min_vertex, path = bbtourists.branch_and_bound()

  print ("Scenario #{}".format(str(c+1)))
  min_trips = math.ceil(num_tourists/(min_vertex-1))
  print ("Minimum Number of Trips = {}".format(str(min_trips)))
  print ()
