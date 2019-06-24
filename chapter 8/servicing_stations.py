def bfs(graph, root):
    visited, queue, seen = [], [root], []
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in visited and w not in seen:
                visited.append(w)
                seen.append(w)
                for x in graph[w]:
                  seen.append(x)
                queue.append(w)
    return visited

class AllSolsBacktrackingStations:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.num_towns = len(puzzle)

  def is_complete(self, s):
    temp_array = [0 for x in range(self.num_towns)]
    for num in s:
      num_row = self.puzzle[num-1]
      temp_array[num-1] = 1
      for i,x in enumerate(num_row):
        if x==1: temp_array[i] = 1
    if 0 not in temp_array: return True
    else: return False
    
  def branch(self, s):
    branches = []
    temp_array = [0 for x in range(self.num_towns)]
    for num in s:
      num_row = self.puzzle[num-1]
      temp_array[num-1] = 1
      for i,x in enumerate(num_row):
        if x==1: temp_array[i] = 1
    for i,x in enumerate(temp_array):
      if x==0: branches.append(s+[i+1])
    return branches

  def backtracking(self, s):
    # Returns first feasible solution or None
    if self.is_complete(s): yield s
    for sp in self.branch(s):
      #if self.is_promising(sp):
      for spp in self.backtracking(sp):
        yield spp
    
  def solve(self):
    return self.backtracking([])

class BacktrackingStations:
  def __init__(self, puzzle):
    self.puzzle = puzzle
    self.num_towns = len(puzzle)

  def is_complete(self, s):
    temp_array = [0 for x in range(self.num_towns)]
    for num in s:
      num_row = self.puzzle[num-1]
      temp_array[num-1] = 1
      for i,x in enumerate(num_row):
        if x==1: temp_array[i] = 1
    if 0 not in temp_array: return True
    else: return False
    
  def branch(self, s):
    branches = []
    temp_array = [0 for x in range(self.num_towns)]
    for num in s:
      num_row = self.puzzle[num-1]
      temp_array[num-1] = 1
      for i,x in enumerate(num_row):
        if x==1: temp_array[i] = 1
    for i,x in enumerate(temp_array):
      if x==0: branches.append(s+[i+1])
    #branches.sort(key=lambda x: x[1], reverse=True)
    #sorted_branches = [x for x,y in branches]
    return branches

  def backtracking(self, s):
    # Returns first feasible solution or None
    if self.is_complete(s): return s
    for sp in self.branch(s):
      #if self.is_promising(sp):
      found = self.backtracking(sp)
      if found != None: return found
    return None
    
  def solve(self):
    return self.backtracking([])

def read_input2():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        if aux_line == "":
          cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          

        town_array = [[0 for x in range(num_towns)] for y in range(num_towns)]
        for x in range(num_town_pairs):
          town1, town2 = (int(x) for x in input().strip().split(" "))
          town_array[town1-1][town2-1] = 1
          town_array[town2-1][town1-1] = 1 
    except EOFError:
      pass  

def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        if aux_line == "":
          cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          

        town_array = {y+1:[] for y in range(num_towns)}
        town_array[0] = [y+1 for y in range(num_towns)]
        for x in range(num_town_pairs):
          town1, town2 = (int(x) for x in input().strip().split(" "))
          town_array[town1].append(town2)
          town_array[town2].append(town1) 
    except EOFError:
      pass

def findrowsum(row, visited_rows):
  new_row = row
  for i,x in enumerate(visited_rows):
    if x == 1: new_row[i] = 0
  return sum(new_row)

def add2rows(row1, row2):
  new_row = row1
  for i, elem in enumerate(row2):
    if elem!=0: new_row[i] = elem
  return new_row

def is_complete(q, graph):
  original_state = [0 for x in range(len(graph))]
  for num in q:
    original_state = add2rows(original_state, graph[num-1])
  if 0 not in original_state:
    return True
  else:
    return False

def recursive_stations_memoized(state, graph):
  R = {}
  def M(q):
    if is_complete(q, graph): R[str(q)] = 0
    else:
      for x in range(len(graph)):
        if x+1 not in q: 
          if str(q+[x+1]) not in R: M(q+[x+1])
      R[str(q)] = min( R[str(q+[x+1])]+1 for x in range(len(graph)) if x+1 not in q)
    return R[str(q)]
  return M(state)

def recursive_stations_memoized(state, graph):
  R = {}
  def M(q):
    if is_complete(q, graph): R[str(q)] = 0
    else:
      for x in range(len(graph)):
        if x+1 not in q: 
          if str(q+[x+1]) not in R: M(q+[x+1])
      R[str(q)] = min( R[str(q+[x+1])]+1 for x in range(len(graph)) if x+1 not in q)
    return R[str(q)]
  return M(state)

puzzles = read_input2()

for puzzle in puzzles:
  print (recursive_stations_memoized([], puzzle))

"""
for puzzle in [puzzles[0]]:
  min_len, min_bfs = 100000000, None
  for x in range(len(puzzle)):
    new_bfs = bfs(puzzle, x)
    if len(new_bfs)+1 < min_len:
      min_len, min_bfs = len(new_bfs)+1, new_bfs+[x]
  print (min_len, min_bfs)
  #print (recursive_min_path(puzzle, len(puzzle)-1))
  #print (breadth_first_search(puzzle, 0))

class town_connections():
  def __init__(self, number, graph):
    self.id = number
    self.state = []
    self.connections = graph[number-1]
    self.graph = graph

  def cost(self):
    return len(self.state)

  def add_station(town):
    if self.connections[town-1] == 0:

"""

"""
  min_sol, aux_sol = 100000, None
  for x in range(len(puzzle)):
    sol = get_greedy_path([], puzzle)
    if len(sol)< min_sol:
      min_sol, aux_sol = len(sol), sol
  print (min_sol)
  
  min_sol, aux_sol = 10000, None
  for sol in AllSolsBacktrackingStations(puzzle).solve():
    if len(sol) < min_sol:
      min_sol, aux_sol = len(sol), sol

  print (min_sol)



def read_input2():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        if aux_line == "":
          cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          

        town_array = [[0 for x in range(num_towns)] for y in range(num_towns)]
        for x in range(num_town_pairs):
          town1, town2 = (int(x) for x in input().strip().split(" "))
          town_array[town1-1][town2-1] = 1
          town_array[town2-1][town1-1] = 1 
    except EOFError:
      pass  

def read_input(): 
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        if aux_line == "":
          cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          

        town_array = {y+1:[] for y in range(num_towns)}
        town_array[0] = [y+1 for y in range(num_towns)]
        for x in range(num_town_pairs):
          town1, town2 = (int(x) for x in input().strip().split(" "))
          town_array[town1].append(town2)
          town_array[town2].append(town1) 
    except EOFError:
      pass

def findrowsum(row, visited_rows):
  new_row = row
  for i,x in enumerate(visited_rows):
    if x == 1: new_row[i] = 0
  return sum(new_row)

def add2rows(row1, row2):
  new_row = row1[:]
  for i, elem in enumerate(row2):
    if elem!=0: new_row[i] = elem
  return new_row

def is_complete(q, graph):
  original_state = [0 for x in range(len(graph))]
  for num in q:
    original_state = add2rows(original_state, graph[num-1])
  if 0 not in original_state:
    return True
  else:
    return False

class station_network():

  def __init__(self, graph, stations=[]):
    self.num_stations = len(stations)
    self.stations = stations
    self.graph = graph
    self.missing_stations = self.get_missing_stations(stations)

  def get_missing_stations(self, stations):
    missing_stations = [x+1 for x in range(len(self.graph))]
    for num in stations:
      for i,x in enumerate(self.graph[num-1]):
        if x==1:
          if i in missing_stations: missing_stations.remove(i)
    return missing_stations

  def add_station(self, town):
    if town not in self.stations:
      self.stations.append(town)
      self.missing_stations = self.get_missing_stations(self.stations)
      self.num_stations += 1

  def cost(self, station = None):
    if station == None:
      return self.num_stations+len(self.missing_stations)
    else:
      return self.num_stations+len(self.get_missing_stations(self.stations+[station]))

  def is_complete(self):
    return len(self.missing_stations)==0

def recursive_stations_memoized(graph):
  stations_array = [station_network(graph) for x in range(len(graph)+1)]
  cost_array = [x.cost() for x in stations_array]
  print (cost_array)
  while True:
    for x in range(len(stations_array)):
      if x>0: 
        if stations_array[x].is_complete(): return stations_array[x].cost()
        else:
          min_cost, aux_min = 10000, None
          for y in range(len(graph)):
            if y not in stations_array[x].stations:
              cost = stations_array[x].cost(y+1)
              if cost < min_cost:
                min_cost, aux_min = cost, y+1
          stations_array[x].add_station(aux_min)

    cost_array = [x.cost() for x in stations_array]
    print (cost_array)


def recursive_stations_memoized(state, graph):
  def M(stations):
    if stations.is_complete(): return 0
    else: min( R[str(q+[x+1])]+1 for x in range(len(graph)) if x+1 not in q)
    return R[str(q)]
  return M(state)

def recursive_stations(graph):
  N = len(graph)
  cities_placed = [0 for x in range(N+1)]
  cities_covered = [0 for x in range(N+1)]
  for i in range(1,N+1):
    for j in range(1, N+1):
      cities_covered[i] = cities_covered[i-1] + max(sum(row) for i,row in enumerate(graph)) 

def get_max_cities_covered(num_stations, graph):
  cities_covered = [0 for x in range(len(graph))]
  max_cities, aux_max = cities_covered[:], None
  added_stations = []
  for x in range(num_stations):
    for i, row in enumerate(graph):
      if i+1 not in added_stations:
      new_covered = add2rows(cities_covered, row)
      if sum(new_covered)>sum(max_cities):
        max_cities, aux_max = new_covered, i+1

    added_stations.append(aux_max)
    cities_covered = max_cities
    if 0 not in cities_covered:
      break
  return (added_stations, cities_covered)



puzzles = read_input2()

for puzzle in puzzles:
  max_cities_array, found = [], False
  for x in range(len(puzzle)):
    if x==0:max_cities_array.append(get_max_cities_covered(x+1, puzzle))
    else: 
      new_tup = get_max_cities_covered(x+1, puzzle)
      if new_tup == max_cities_array[-1]:
        print (len(new_tup[0]))
        found = True
        break
      else: max_cities_array.append(new_tup)
  if not found:
    print (max_cities_array[-1])


#print (recursive_stations_memoized(puzzles[7]))


  """

