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

        town_array = [[0 if x==y else -2**31 for x in range(num_towns)] for y in range(num_towns)]
        
        for x in range(num_town_pairs):
          town1, town2, capacity = (int(x) for x in input().strip().split(" ") if x!="")
          town_array[town1-1][town2-1] = capacity
          town_array[town2-1][town1-1] = capacity
        start_city, end_city, num_tourists = (int(x) for x in input().strip().split(" ") if x!="")

        cases.append((town_array, start_city, end_city, num_tourists))

    except EOFError:
      pass

def tourist_dp(graph):
  dp = graph
  N = len(graph)
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dp[i][j] = max(dp[i][j], min(dp[i][k], dp[k][j]))

  return dp


puzzles = read_input()

print (puzzles[0])

"""
for c,puzzle_arr in enumerate(puzzles):
  puzzle = puzzle_arr[0]
  start_city, end_city = puzzle_arr[1], puzzle_arr[2]
  num_tourists = puzzle_arr[3]

  min_cost = tourist_dp(puzzle)[start_city-1][end_city-1]

  print ("Scenario #{}".format(str(c+1)))
  min_trips = math.ceil(num_tourists/(min_cost-1))
  print ("Minimum Number of Trips = {}".format(str(min_trips)))
  print ()
"""