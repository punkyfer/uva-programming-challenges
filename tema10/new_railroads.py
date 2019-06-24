
class edge():
  def __init__(self, to, start_time, end_time):
    self.to = to
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return str(self.start_time) + " - " + str(self.end_time) + " (" + str(self.to) + ")"


def memoized_railroads(g, start_city, end_city, start_time, num_cities, maxtime):
  dist = [[-1]*105 for y in range(maxtime+1)]
  for i in range(len(g[start_city])):
    if g[start_city][i].start_time >= start_time:
      dist[g[start_city][i].end_time][g[start_city][i].to] = max(dist[g[start_city][i].end_time][g[start_city][i].to], g[start_city][i].start_time)

  for i in range(start_time, maxtime+1):
    for j in range(num_cities):
      for k in range(len(g[j])):
        if g[j][k].start_time >= i:
          dist[g[j][k].end_time][g[j][k].to] = max(dist[g[j][k].end_time][g[j][k].to], dist[i][j])

    if dist[i][end_city] != -1:
      return (dist[i][end_city], i)
  return None, None

def convert_string(time):
  res = str(time)
  while (len(res) < 4):
    res = '0'+res
  return res

def read_input():
  cases = []
  try:
    while(True):
      num_scenarios = int(input().strip())
      for num_scenario in range(num_scenarios):
        num_cities = int(input().strip())
        edges = [[] for x in range(105)]
        maxtime = 0

        cities_map = {}

        for city_num in range(num_cities):
          cities_map[input().strip()] = city_num
          edges[city_num] = []

        num_train_descs = int(input().strip())

        for ntd in range(num_train_descs):
          num_stops = int(input().strip())

          for ns in range(num_stops):
            aux_line = input().strip()
            time, cityName = int(aux_line.split()[0]), aux_line.split()[1]
            y = cities_map[cityName]
            if ns and time>=ptime:
              edges[x].append(edge(y, ptime, time))
            x = y
            ptime = time
            if time > maxtime:
              maxtime = time

        start_time = int(input().strip())

        start_city = input().strip()
          
        end_city = input().strip()

        x = cities_map[start_city]
        y = cities_map[end_city]


        cases.append((edges, start_city, end_city, x, y, start_time, num_cities, maxtime))
  except EOFError:
    pass
  return cases

cases = read_input()

for i, case in enumerate(cases):
  print ("Scenario", i+1)

  edges, start_city, end_city, sc_x, ec_y, start_time, num_cities, maxtime = case

  departure_time, arrival_time = memoized_railroads(edges, sc_x, ec_y, start_time, num_cities, maxtime)
  if departure_time == None or arrival_time==None:
    print ("No connection")
  else:
    print ("Departure {} {}".format(convert_string(departure_time), start_city))
    print ("Arrival   {} {}".format(convert_string(arrival_time), end_city))

  print ()