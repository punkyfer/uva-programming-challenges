debug = False

class Graph():

  def __init__(self, num_intersections, stations):
    self.intersections = [x+1 for x in range(num_intersections)]
    self.neighbours = {x:[] for x in self.intersections}
    self.edge_cost = {x:{} for x in self.intersections}
    self.stations = stations

  def add_edge(self, node_1, node_2, cost):
    self.neighbours[node_1] += [node_2]
    self.neighbours[node_2] += [node_1]
    self.edge_cost[node_1][node_2] = cost
    self.edge_cost[node_2][node_1] = cost

  def dijkstra(self, source_nodes, prev_dist = None):
    inf = 2**31
    if prev_dist==None: dist = {x:inf for x in self.intersections}
    else: dist = dict(prev_dist)
    for source_node in source_nodes:
      dist[source_node] = 0
    node_queue = set([source_node])
    visited = set()

    while node_queue:
      min_node = node_queue.pop()
      visited.add(min_node)
      for neighbour_node in self.neighbours[min_node]:
        if neighbour_node not in visited:
          if dist[min_node]+self.edge_cost[min_node][neighbour_node] < dist[neighbour_node]:
            dist[neighbour_node] = dist[min_node]+self.edge_cost[min_node][neighbour_node]

          node_queue.add(neighbour_node)

    return dist

  def find_station(self):
    if self.stations:
      dist = self.dijkstra(self.stations)
      min_cost = sum(dist.values())
    else:
      dist = None
      min_cost = 2 ** 31
    min_node = 0

    if debug:
      print (dist)
      print (min_cost)
      print ("-------")

    for node in self.intersections:
      if node not in self.stations:
        new_dist = self.dijkstra([node], dist)
        cost = sum(new_dist.values())
        if debug: 
          print (node)
          print (new_dist)
          print (cost)
          print ("-------")
        if cost < min_cost:
          min_cost = cost
          min_node = node

    return min_node




def read_input():

  num_cases = int(input())

  cases = []
  for case in range(num_cases):
    aux_line = input().strip() # Blank Line
    while not aux_line: aux_line = input().strip()
    num_stations, num_intersections = (int(x) for x in aux_line.split())
    stations = []
    for x in range(num_stations):
      stations += [int(x) for x in input().split()]
    graph = Graph(num_intersections, stations)

    aux_line = input().strip()
    while aux_line:
      node_1, node_2, cost = (int(x) for x in aux_line.split())
      graph.add_edge(node_1, node_2, cost)
      try: aux_line = input().strip()
      except EOFError: break

    cases += [graph]

  return cases


cases = read_input()

for case in cases:
  if len(case.intersections) == 1 or case.intersections == case.stations:
    print (case.intersections[0])
  else:
    print (case.find_station())
  print ()
