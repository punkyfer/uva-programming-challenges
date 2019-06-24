def read_input():
  cases = []

  while(True):
    n = int(input())

    if n == 0:
      break

    points = []
    for i in range(n):
      points += [[int(x) for x in input().split()]]

    points += [points[0]]
    cases += [points]

  return cases

def gcd(x, y):
  while(y):
    x, y = y, x % y

  return x

def get_area_and_num_points(points):
  lsum = 0
  rsum = 0
  num_points = 0
  for i in range(len(points)):
    if i < len(points)-1:
      lsum += points[i][0] * points[i+1][1]
      rsum += points[i][1] * points[i+1][0] 

    if i > 0:
      num_points += gcd(abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1]))

  return 0.5 * abs(lsum-rsum), num_points

def find_interior_points(points):
  area, num_points = get_area_and_num_points(points)
  return int(area - (num_points*0.5) + 1)


cases = read_input()

for case in cases:
  print (find_interior_points(case))