def read_input():

  cases = []

  while True:
    try:
      rows, columns = (int(x) for x in input().split())
      num_ints = 0
      matrix = []
      nums = []
      while len(nums) < rows * columns:
        tmp = [int(x) for x in input().split()]
        nums += tmp
      ctr = 0
      while ctr < len(nums):
        matrix += [nums[ctr:columns + ctr]]
        ctr += columns
      cases += [matrix]
    except EOFError:
      break

  return cases

def build_path(row, cost):
  path = [row]
  for j in range(len(cost[0])-1):
    prow = path[-1]-1
    if prow == 0:
      values = [cost[prow][j+1], cost[prow+1][j+1], cost[len(cost)-1][j+1]]
      index_min = min(range(len(values)), key=values.__getitem__)
      if index_min == 2:
        trow = len(cost)-1
      else:
        trow = prow + index_min
    elif prow == len(cost)-1:
      values = [cost[0][j+1], cost[prow-1][j+1], cost[prow][j+1]]
      index_min = min(range(len(values)), key=values.__getitem__)
      if index_min == 0:
        trow = 0
      else:
        if index_min == 1:
          trow = prow - 1
        else:
          trow = prow
    else:
      values = [cost[prow-1][j+1],cost[prow][j+1], cost[prow+1][j+1]]
      index_min = min(range(len(values)), key=values.__getitem__)
      if index_min == 0:
        trow = prow - 1
      else:
        if index_min == 2:
          trow = prow + 1
        else:
          trow = prow

    path += [trow+1]

  return path


def memoized_tsp(matrix):
  cost = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

  for i in range(len(matrix)):
    cost[i][len(matrix[0])-1] = matrix[i][len(matrix[0])-1]
    
  final_cost = 2**31
  min_row = 0
  for j in range(len(matrix[0])-2, -1, -1):
    for i in range(len(matrix)):
      if i == 0:
        mc = min(cost[len(matrix)-1][j+1], cost[i][j+1], cost[i+1][j+1]) + matrix[i][j]
      elif i == len(matrix)-1:
        mc = min(cost[i-1][j+1], cost[i][j+1], cost[0][j+1]) + matrix[i][j]
      else:
        mc = min(cost[i-1][j+1], cost[i][j+1], cost[i+1][j+1]) + matrix[i][j]

      cost[i][j] = mc

      if j == 0 and mc < final_cost:
        final_cost = mc
        min_row = i+1

  path = build_path(min_row, cost)
  return path, final_cost


for case in read_input():
  min_path, final_cost = memoized_tsp(case)

  print (str(min_path)[1:-1].replace(' ','').replace(',',' '))
  print (final_cost)