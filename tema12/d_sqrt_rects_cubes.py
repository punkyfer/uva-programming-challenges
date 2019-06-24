def read_input():
  cases = []
  while True:
    try:
      side_length = int(input())
      cases += [side_length]
    except EOFError:
      break
  return cases

def get_nums(side_length, n_dims = 3):
  n_cubes = [0 for x in range(n_dims)]
  n_rectangles = [0 for x in range(n_dims)]

  for n in range(1, side_length+1):
    n_cubes[0] += n * n
    n_cubes[1] += n * n * n
    n_cubes[2] += n * n * n * n

  t = side_length * (side_length+1) / 2
  n_rectangles[0] = t * t - n_cubes[0]
  n_rectangles[1] = t * t * t - n_cubes[1]
  n_rectangles[2] = t * t * t * t - n_cubes[2]

  return n_rectangles, n_cubes

cases = read_input()

for case in cases:
  n_rectangles, n_cubes = get_nums(case)
  print ("{} {} {} {} {} {}".format(
    int(n_cubes[0]), int(n_rectangles[0]), 
    int(n_cubes[1]), int(n_rectangles[1]), 
    int(n_cubes[2]), int(n_rectangles[2])))