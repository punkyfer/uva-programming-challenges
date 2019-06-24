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

def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()
        while aux_line=="":
          aux_line = input().strip()
        num_scenarios = int(aux_line)
        for x in range(num_scenarios):
          aux_line = input().strip()
          while aux_line=="":
            aux_line = input().strip()
          num_cities = int(aux_line)

          cities_map = {}

          for y in range(num_cities):
            aux_line = input().strip()
            while aux_line=="":
              aux_line = input().strip()
            cities_map[aux_line] = (y, City(aux_line))

          aux_line = input().strip()
          while aux_line=="":
            aux_line = input().strip()
          num_train_descs = int(aux_line)

          timetable = []
          for y in range(num_train_descs):
            aux_line = input().strip()
            while aux_line=="":
              aux_line = input().strip()
            num_connections = int(aux_line) 
            aux_table = []           
            for l in range(num_connections):
              aux_line = input().strip()
              while aux_line=="":
                aux_line = input().strip()
              time, city = int(aux_line.split()[0]), aux_line.split()[1]
              aux_table.append((time, city))
            timetable.append(aux_table)

          for timetable_row in timetable:
            for y in range(len(timetable_row)):
              time, city = timetable_row[y]
              for z in range(y+1, len(timetable_row)):
                ntime, ncity = timetable_row[z]
                cities_map[city][1].add_connection(ncity, (time, ntime))
                cities_map[ncity][1].add_start_time(ntime)

          aux_line = input().strip()
          while aux_line=="":
            aux_line = input().strip()
          start_time = int(aux_line)

          aux_line = input().strip()
          while aux_line=="":
            aux_line = input().strip()
          start_city = aux_line

          aux_line = input().strip()
          while aux_line=="":
            aux_line = input().strip()
          end_city = aux_line

          cities_map[start_city][1].add_start_time(start_time)

          weighted_array = [[0 for x in range(num_cities)] for y in range(num_cities)]
          for city in cities_map:
            pos = cities_map[city][0]
            for neighbour in cities_map[city][1].get_neighbours():
              npos = cities_map[neighbour][0]
              weighted_array[pos][npos] = cities_map[city][1].get_trip_cost(neighbour)

          cases.append((weighted_array, cities_map, start_time, start_city, end_city))
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

def w_algo(cities_map, start_city, end_city, start_time):
  dp = [{x:x for x in cities_map} for y in range(2400)]

  dp[start_time][start_city] = 1
  min_con = 2**31
  Q = [start_city]
  while len(Q)>0:
    city = Q.pop(0)
    for connection in cities_map[city][1].connections:
      stime, etime = cities_map[city][1].connections[connection]
      if stime > start_time and etime > start_time:
        #dp[stime][city] = etime
        dp[etime][connection] = city
        Q.append(connection)
  
  num_cons = 0
  path = []


  for i, row in enumerate(dp):
    if list(row.values()) != [x for x in cities_map]:
      print (i, row)
      num_cons+=1


def tourist_dp(graph):
  dp = graph
  N = len(graph)
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dp[i][j] = max(dp[i][j], min(dp[i][k], dp[k][j]))

  return dp

class Route():
  def __init__(self, from_city, to_city, start_time, end_time):
    self.from_city = from_city
    self.to_city = to_city
    self.start_time = start_time
    self.end_time = end_time

class Graph():
  def __init__(self, start_time, start_city, end_city):
    self.start_time = start_time
    self.start_city = start_city
    self.end_city = end_city
    self.schedules = {}

  def add_schedule(self, town, neighbour, stime, etime):
    if town in self.schedules.keys():
      self.schedules[town].append(Route(town, neighbour, stime, etime))
    else:
      self.schedules[town] = [Route(town, neighbour, stime, etime)]

  def get_schedules(self, town):
    if town in self.schedules.keys():
      return self.schedules[town]
    else:
      return None


def convert_path(parent, start_city, end_city, cities_map):
  num2city = {}
  for city in cities_map:
    num2city[cities_map[city][0]]=city

  path = [end_city]
  while start_city not in path:
    path.append(parent[path[-1]])

  new_path = []
  for num in path[::-1]:
    new_path.append(num2city[num])
  return new_path

cases = read_input()

def convert_time(time):
  time = str(time)
  while len(time)<4:
    time ='0'+time
  return time

for i, case in enumerate(cases):
  print ("Scenario",i+1)

  weighted_array, cities_map, start_time, start_city, end_city = case

  """
  w_algo(cities_map, start_city, end_city, start_time)
  dp = tourist_dp(weighted_array)
  for row in dp:
    print (row)
  print (dp[cities_map[start_city][0]][cities_map[end_city][0]])
  """

  parent, dist = Dijkstra(weighted_array, cities_map[start_city][0], cities_map[end_city][0])

  print (dist)

  if dist == 2**31:
    print ("No connection")
  else:
    path = convert_path(parent, cities_map[start_city][0], cities_map[end_city][0], cities_map)
    departure = cities_map[path[0]][1].get_schedule(path[1])[0]
    arrival = cities_map[path[-2]][1].get_schedule(path[-1])[1]

    if departure < start_time:
      print ("No connection")
    else:
      departure = convert_time(departure)
      arrival = convert_time(arrival)
      print ("Departure", departure, path[0])
      print ("Arrival  ", arrival, path[-1])
  print ()
