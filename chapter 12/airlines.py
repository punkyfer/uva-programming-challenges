from math import sin, cos, acos
PI = 3.141592653589793/180
EARTH_RADIUS = 6378.0

class City():
  def __init__(self, lattitude, longitude):
    self.lat = lattitude
    self.lon = longitude

  def dist(self, other):
    lat1, lat2 = PI * self.lat, PI * other.lat
    lon1, lon2 = PI * self.lon, PI * other.lon
    cs = cos(lat1)*cos(lat2)*cos(lon2-lon1) + sin(lat1)*sin(lat2)
    dist = EARTH_RADIUS*acos(cs)
    return int(dist+0.5)

def airlines_dp(dist, num_cities):
  for k in range(num_cities):
    for i in range(num_cities):
      for j in range(num_cities):
        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
  return dist

def read_input():
  cases = []
  try:
    while(True):
      aux_line = input().strip()
      num_cities, num_connections, num_queries = (int(x) for x in aux_line.split())
      if num_cities==num_connections and num_connections==num_queries and num_queries==0:
        return cases

      dist = [[2**31 for j in range(num_cities)] for i in range(num_cities)]
      cities=[]
      cities_map={}

      for i in range(num_cities):
        aux_line = input().strip()
        cname = aux_line.split()[0]
        lat, lon = float(aux_line.split()[1]), float(aux_line.split()[2])
        cities.append(City(lat, lon))
        cities_map[cname]=i
        dist[i][i] = 0

      for i in range(num_connections):
        scity, ecity = input().strip().split()
        x, y = cities_map[scity], cities_map[ecity]


        dist[x][y] = cities[x].dist(cities[y])

      queries = []
      for i in range(num_queries):
        scity, ecity = input().strip().split()
        queries.append((scity, ecity))

      cases.append((cities, cities_map, dist, queries))

  except EOFError:
    pass
  return cases

cases = read_input()

for i, case in enumerate(cases):
  print ("Case #{}".format(str(i+1)))

  cities, cities_map, dist, queries = case

  dist = airlines_dp(dist, len(cities))

  for query in queries:
    x, y = cities_map[query[0]], cities_map[query[1]]
    if dist[x][y] == 2**31:
      print ("no route exists")
    else:
      print ("{} km".format(dist[x][y]))
  if i+1<len(cases):
    print()

