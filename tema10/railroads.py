from collections import defaultdict, namedtuple
from operator import itemgetter
from heapq import heappop, heappush

class City():
  def __init__(self, name):
    self.name = name
    self.connections = {}
    self.start_time = 2**31

  def get_neighbours(self):
    return list(self.connections.keys())

  def add_connection(self, city, schedule):
    if city != self.name:
      self.connections[city]=schedule

  def get_trip_cost(self, city):
    if city not in self.get_neighbours():
      return 2**31
    else:
      schedule = self.connections[city]
      if schedule[0] < self.start_time:
        cost = 2**31
      else:
        cost = schedule[0]-self.start_time + schedule[1]-schedule[0]

    return cost

  def print_info(self):
    print ("Name: ",self.name)
    print ("Neighbours: ", self.get_neighbours())
    print ("Start time: ", self.start_time)
    for connection in self.connections:
      print (connection, self.connections[connection])

    for neighbour in self.get_neighbours():
      print (self.get_trip_cost(neighbour))

  def add_start_time(self, time):
    if time < self.start_time:
      self.start_time = time

  def get_schedule(self, city):
    if city in self.connections.keys():
      return self.connections[city]
    else:
      return None

def read_train(cities):
  num_stops = int(input().strip())
  stops = []
  if num_stops > 1:
    for s in range(num_stops):
      time, city = input().strip().split()
      stops.append((cities[city], int(time)))
  return stops

def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        num_scenarios = int(aux_line)
        for x in range(num_scenarios):
          num_cities = int(input().strip())

          cities = [input().strip() for _ in range(num_cities)]
          rcities = {city:i for i,city in enumerate(cities)}

          num_trains = int(input().strip())
          trains = [read_train(rcities) for t in range(num_trains)]

          start_time = int(input().strip())

          start_city = rcities[input().strip()]
          
          end_city = rcities[input().strip()]
          
          cases.append((cities, trains, start_time, start_city, end_city))
        return cases
    except EOFError:
      pass

def get_neighbours(graph, node):
  neighbours = []
  for i,x in enumerate(graph[node]):
    if x!=0:
      neighbours.append(i)
  return neighbours 

def Dijkstra(graph, source, end):
  dist = {source:0}
  Q = []
  path = []
  parent = {}
  for v in range(len(graph)):
    if v != source:
      dist[v] = 2**31
    Q.append(v)  

  while len(Q)>0:
    min_dist, min_vertex = dist[Q[0]], Q[0]
    for v in Q:
      if dist[v]<min_dist:
        min_dist, min_vertex = dist[v], v
    Q.remove(min_vertex)

    for neighbour in get_neighbours(graph, min_vertex):
      alt = dist[min_vertex]+graph[min_vertex][neighbour]
      if alt < dist[neighbour]:
        dist[neighbour] = alt
        parent[neighbour] = min_vertex

  return parent, dist[end]


def get_departure_time(parent, start_city, end_city, cities_map, city_nums):

  path = [end_city]
  while start_city not in path:
    path.append(parent[path[-1]])

  departure = cities_map[city_nums[path[-1]]][1].get_schedule(city_nums[path[-2]])[0]

  return departure

cases = read_input()

def convert_time(time):
  time = str(time)
  if len(time)==1:
    time = '000'+time
  elif len(time)==2:
    time = '00'+time
  elif len(time)==3:
    time = '0'+time
  return time

ARRIVAL = 'arrival'
DEPARTURE = 'departure'
Connection = namedtuple("Connection", ['departure', 'arrival', 't_departure', 't_arrival', 'uid'])

def con_start_id(con):
    """id used for connection departure node after time expansion"""
    return con.uid*2
    
def con_end_id(con):
    """id used for connection arrival node after time expansion"""
    return con.uid*2+1

def build_connection_table(trains, start_time=0):
    """
    Build dictionary with a list of arrivals and departures for each city
    con, city_table = bould_connection_table(....)
    city_table[city_id, ARRIVAL]
    city_table[city_id, DEPARTURE]
    Arguments:
        trains (list): List of trains provided through stdin
        start_time (int): All connections departing or arriving sooner than
            this time will be ignored.
    Returns:
        connections: List of all valied connections
        cities: city arrival/departure connection dict 
    """
    # Per city
    cuid = 0 # Connection unique id
    
    # List of connections ordered by id 
    connections = [] 

    # Dictionary of connections by city separated by arrival/departure
    cities = defaultdict(list)

    for schedule in trains:
        # TODO: Use zip
        prev_city, prev_time = schedule[0]
        for city, time in schedule[1:]:
            if prev_time >= start_time:
                con = Connection(prev_city, city, prev_time, time, cuid)
                cities[(city, ARRIVAL)].append(con)
                cities[(prev_city, DEPARTURE)].append(con)
                connections.append(con)
                cuid += 1
            prev_city, prev_time = city, time

    return connections, cities

def build_time_exp_adj(city_connections, connections):
    """Build time expanded adjacency list
    
    Arguments:
        city_connections (dict): city arrival/departure connection dict
        connections (list): List of all valid connections
    
    Returns:
        adjList
    """
    adjList = [list() for _ in range(2*len(connections))]

    # Add intercity connections (departure-arrival)
    for c in connections:
        adjList[con_start_id(c)].append((con_end_id(c), c.t_arrival-c.t_departure, c))

    # Add intracity connections, delays inside city waiting until some train departure
    for city in range(len(city_connections)//2):
        times = []

        # Append arrivals first so they are sorted first when the time
        # is the same as one departure.
        for c in city_connections[city, ARRIVAL]:
            times.append((c.t_arrival, con_end_id(c), c))
        for c in city_connections[city, DEPARTURE]:
            times.append((c.t_departure, con_start_id(c), c))

        if len(times) < 2:
            continue

        times = sorted(times, key=itemgetter(0))
       
        for node, next_node in zip(times, times[1:]):
            adjList[node[1]].append((next_node[1], next_node[0]-node[0], None))

    return adjList

for i, case in enumerate(cases):
  print ("Scenario",i+1)

  cities, trains, start_time, start_city, end_city = case

  con_table, citie_cons = build_connection_table(trains, start_time)
  adj_list = build_time_exp_adj(citie_cons, con_table)

  for row in adj_list:
    print (row)
"""
  parent, dist = Dijkstra(weighted_array, cities_map[start_city][0], cities_map[end_city][0])

  if dist == 2**31:
    print ("No connection")
  else:
    departure = get_departure_time(parent, cities_map[start_city][0], cities_map[end_city][0], cities_map, city_nums)
    arrival = start_time + dist

    if departure < start_time:
      print ("No connection")
    else:
      departure = convert_time(departure)
      arrival = convert_time(arrival)
      print ("Departure", departure, start_city)
      print ("Arrival  ", arrival, end_city)
  print ()
"""