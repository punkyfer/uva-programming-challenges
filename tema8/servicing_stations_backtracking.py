def add2rows(row1, row2):
  new_row = row1[:]
  for i, elem in enumerate(row2):
    if elem!=0: new_row[i] = elem
  return new_row

def get_greedy_path(state, graph):
  cities_covered = [0 for x in range(len(graph))]
  for num in state:
    cities_covered = add2rows(cities_covered, graph[num-1])
  max_cities, aux_max = cities_covered[:], None
  added_stations = state
  while 0 in cities_covered:
    for i, row in enumerate(graph):
      if i+1 not in added_stations:
        new_covered = add2rows(cities_covered, row)
        if sum(new_covered)>sum(max_cities):
          max_cities, aux_max = new_covered, i+1

    added_stations.append(aux_max)
    cities_covered = max_cities
    if 0 not in cities_covered:
      break
  return len(added_stations)

                    
def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()

        while aux_line == "":
          if town_array not in cases:
            cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          
        if num_town_pairs == 0 and num_towns != 0:
          town_array = [num_towns]
        else:
          if num_town_pairs >= num_towns*(num_towns-1)/2:
            town_array = [1]
          else:
            town_array = [[0 for x in range(num_towns)] for y in range(num_towns)]
            for x in range(num_towns):
              town_array[x][x] = 1
            for x in range(num_town_pairs):
              town1, town2 = (int(x) for x in input().strip().split(" ") if x!="")
              town_array[town1-1][town2-1] = 1
              town_array[town2-1][town1-1] = 1 
    except EOFError:
      pass

puzzles = read_input()
for puzzle in puzzles:
  if len(puzzle) == 1:
    print ( puzzle[0])
  else:
    min_cost = 2**31
    for x in range(len(puzzle)):
      cost = get_greedy_path([x+1], puzzle)
      if cost < min_cost: min_cost=cost

    print (min_cost)
