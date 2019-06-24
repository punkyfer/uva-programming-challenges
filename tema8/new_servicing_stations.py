def add2rows(row1, row2):
  new_row = row1[:]
  for i, elem in enumerate(row2):
    if elem!=0: new_row[i] = elem
  return new_row

def get_greedy_path(state, graph):
  cities_covered = [0 for x in range(len(graph))]
  for num in state:
    cities_covered = add2rows(cities_covered, graph[num-1])
  max_cities, aux_max = cities_covered[:], None
  added_stations = state
  while 0 in cities_covered:
    for i, row in enumerate(graph):
      if i+1 not in added_stations:
        new_covered = add2rows(cities_covered, row)
        if sum(new_covered)>sum(max_cities):
          max_cities, aux_max = new_covered, i+1

    added_stations.append(aux_max)
    cities_covered = max_cities
    if 0 not in cities_covered:
      break
  return len(added_stations)
                    
def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()

        while aux_line == "":
          if town_array not in cases:
            cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          
        if num_town_pairs == 0 and num_towns != 0:
          town_array = [num_towns]
        else:
          town_array = [[0 for x in range(num_towns)] for y in range(num_towns)]
          for x in range(num_towns):
            town_array[x][x] = 1
          for x in range(num_town_pairs):
            town1, town2 = (int(x) for x in input().strip().split(" ") if x!="")
            town_array[town1-1][town2-1] = 1
            town_array[town2-1][town1-1] = 1 
    except EOFError:
      pass

class BranchAndBoundStations:

  def __init__(self, graph):
    self.graph = graph
    self.num_towns = len(graph)

  def is_complete(self, q):
    original_state = [0 for x in range(len(self.graph))]
    for num in q:
      original_state = add2rows(original_state, self.graph[num-1])
    if 0 not in original_state:
      return True
    else:
      return False

  def branch(self, s, weights=False):
    branches = []
    temp_array = [0 for x in range(self.num_towns)]
    for num in s:
      num_row = self.graph[num-1]
      temp_array[num-1] = 1
      for i,x in enumerate(num_row):
        if x==1: temp_array[i] = 1
    for i,x in enumerate(temp_array):
      if x==0: 
        if not weights: branches.append(s+[i+1])
        else: branches.append((s+[i+1], get_greedy_path(s+[i+1], self.graph)))
    return branches

  def sorted_insert(self, active_set, child_tup):
    ctr = 0
    child, child_weight = child_tup
    for node,weight in active_set:
      if weight<child_weight:
        ctr += 1
      else:
        break
    active_set.insert(ctr, child_tup)

  def branch_and_bound(self):
    bestval = get_greedy_path([], self.graph)
    active_set = [([], bestval)]
    currentbest = None
    while len(active_set)!=0:
      node, node_weight = active_set.pop(0)
      children_w = self.branch(node, weights=True)
      prev_children, ctr = 0, 0
      for children, weight in children_w:
        if weight > bestval: pass
        elif self.is_complete(children):
          bestval, currentbest = weight, children
        else: 
          active_set.insert(0, (children, weight))
          #active_set.append((children, weight))
          """
          if weight < node_weight:
            node_weight = weight
            active_set.insert(0, (children, weight))
          else:
            active_set.append((children, weight))
          """
          #self.sorted_insert(active_set, (children, len(children)))
    return bestval, currentbest

puzzles = read_input()

for puzzle in puzzles:
  if len(puzzle)==1: print (puzzle[0])
  else:
    bbstation = BranchAndBoundStations(puzzle)
    best_val, current_best = bbstation.branch_and_bound()
    print (best_val)

"""
for puzzle in puzzles:
  if len(puzzle)==1: print (puzzle[0])
  else:
    min_cost = 2**31
    for x in range(len(puzzle)):
      cost = get_greedy_path([x+1], puzzle)
      if cost < min_cost: min_cost=cost

    print (min_cost)
"""