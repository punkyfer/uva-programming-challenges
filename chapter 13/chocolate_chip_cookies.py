import math

diameter = 50
radius = 25
tray_limit = 501

def float_2_int(num):
  num_str = str(num).split(".")
  return int(num_str[0]+num_str[1])

def get_distance(a, b):
  return math.sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2))

def get_num_chips(point, radius, cookie_points):
  num_chips = 0
  for chip in cookie_points:
    if get_distance(point, chip)<radius:
      num_chips += 1
  return num_chips

def get_neighbours(point, radius):
  neighbours = []
  if point[0]-1 >= 0:
    neighbours.append((point[0]-1, point[1]))
  if point[0]+1 < tray_limit:
    neighbours.append((point[0]+1, point[1]))
  if point[1]-1 >= 0:
    neighbours.append((point[0], point[1]-1))
  if point[1]+1 < tray_limit:
    neighbours.append((point[0], point[1]+1))
  return neighbours

def read_input():
  cases = []
  try:
    while(True):
      num_test_cases = int(input().strip())
      aux_line = input().strip()
      for nt in range(num_test_cases):
        aux_line = input().strip()
        cookie_points = []
        cookie_grid = [[0 for x in range(501)] for y in range(501)]
        while aux_line != "":
          x = float_2_int(aux_line.split()[0])
          y = float_2_int(aux_line.split()[1])
          cookie_grid[y][x] = 1
          cookie_points.append((x,y))
        else:
          cases.append(cookie_grid, cookie_points)

  except EOFError:
    pass
  return cases

cases = read_input()

for case in cases:
  cookie_grid, cookie_points = case

  neighbour_points = []
  for point in cookie_points:
    neighbour_points += get_neighbours(point, radius)
  neighbour_points = list(set(neighbour_points))

  maxNumChips = 0
  for point in neighbour_points:
    num_chips = get_num_chips((point[0],point[1]),radius, cookie_points)
    if num_chips>maxNumChips: maxNumChips = num_chips
  print (maxNumChips)
  print ()