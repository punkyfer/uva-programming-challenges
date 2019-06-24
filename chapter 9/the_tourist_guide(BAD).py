import math

def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        while aux_line=="":
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

def read_input2():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        while aux_line=="":
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          return cases

        town_array = [[0 if x==y else -2**31 for x in range(num_towns)] for y in range(num_towns)]
        
        for x in range(num_town_pairs):
          town1, town2, capacity = (int(x) for x in input().strip().split(" ") if x!="")
          town_array[town1-1][town2-1] = capacity
          town_array[town2-1][town1-1] = capacity
        start_city, end_city, num_tourists = (int(x) for x in input().strip().split(" ") if x!="")

        cases.append((town_array, start_city, end_city, num_tourists))

    except EOFError:
      pass


def process_distance(graph, num_tourists):
  num_towns = len(graph)
  new_graph = [[0 for x in range(num_towns)] for x in range(num_towns)]
  for i in range(num_towns):
    for j in range(num_towns):
      if graph[i][j]!=0: new_graph[i][j] = num_tourists/graph[i][j]

  return new_graph

def get_neighbours(vertex, graph):
  neighbours = []
  for x in range(len(graph)):
    if graph[vertex-1][x] != 0: neighbours.append(x+1)
  return neighbours


def Dijkstra(graph, start):
  dist = {start:0}
  Q = []
  path = {}
  for x in range(len(graph)):
    if x+1 != start:
      dist[x+1] = 2**31
    Q.append(x+1)

  while len(Q)!=0:
    min_dist, aux_min = 2**31, None
    for vertex in Q:
      if dist[vertex] < min_dist:
        min_dist, aux_min = dist[vertex], vertex

    Q.remove(aux_min)
    v = aux_min

    for u in get_neighbours(v, graph):
      alt = dist[v] + graph[v-1][u-1]
      if alt < dist[u]:
        dist[u] = alt
        path[u] = v

  return dist, path



def tourist_dp(graph):
  dp = graph
  N = len(graph)
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dp[i][j] = max(dp[i][j], min(dp[i][k], dp[k][j]))

  return dp


puzzles = read_input2()


for c,puzzle_arr in enumerate(puzzles):
  puzzle = puzzle_arr[0]
  start_city, end_city = puzzle_arr[1], puzzle_arr[2]
  num_tourists = puzzle_arr[3]

  #processed_graph = process_distance(puzzle, num_tourists)
  processed_graph = puzzle

  min_cost = tourist_dp(puzzle)[start_city-1][end_city-1]

  print ("Scenario #{}".format(str(c+1)))
  min_trips = math.ceil(num_tourists/(min_cost-1))
  print ("Minimum Number of Trips = {}".format(str(min_trips)))
  print ()
  """
  distance, paths = Dijkstra(processed_graph, start_city)


  path = [end_city]
  while start_city not in path:
    path.append(paths[path[-1]])

  path = path[::-1]

  print (path)

  min_cost = 100000
  for i,x in enumerate(path[:-1]):
    if puzzle[x-1][path[i+1]-1] < min_cost:
      min_cost = puzzle[x-1][path[i+1]-1]
  
  print ("Scenario #{}".format(str(c+1)))
  min_trips = math.ceil(num_tourists/(min_cost-1))
  print ("Minimum Number of Trips = {}".format(str(min_trips)))
  print ()
  """