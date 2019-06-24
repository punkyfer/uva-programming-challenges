def read_input():
  cases = [[] for x in range(int(input()))]
  for case in cases:
    input()
    for x in range(int(input())):
      case += [int(input())]
  return cases

def solve_for_3_or_less(case):
  if (len(case) == 1):
    return case[0], [[case[0]]]
  elif (len(case) == 2):
    return case[1], [[case[0], case[1]]]
  else:
    return case[1]+case[0]+case[2], [[case[0], case[1]],[case[0]],[case[0], case[2]]]

def solve_case(case):
  crossing_cost = 0
  crossings = []
  not_crossed = sorted(case)
  while (len(not_crossed) != 0):
    if (len(not_crossed) < 4):
      t_cost, t_crossings = solve_for_3_or_less(not_crossed)
      crossing_cost += t_cost
      crossings += t_crossings
      not_crossed = []
    else:
      people = not_crossed[0:2] + not_crossed[-2:]
      a_cost, a_trips = strategy_a(people)
      b_cost, b_trips = strategy_b(people)
      if (a_cost < b_cost):
        crossings += a_trips
        crossing_cost += a_cost
      else:
        crossings += b_trips
        crossing_cost += b_cost
      not_crossed = not_crossed[:-2]

  return crossing_cost, crossings

def strategy_a(people):
  trips = [
    [people[0],people[1]],
    [people[0]],
    [people[2],people[3]],
    [people[1]]
    ]
  cost = people[0]+people[3]+people[1]*2
  return cost, trips

def strategy_b(people):
  trips = [
    [people[0], people[2]],
    [people[0]],
    [people[0], people[3]],
    [people[0]]
    ]
  cost = 2*people[0]+people[2]+people[3]
  return cost, trips


cases = read_input()

for i, case in enumerate(cases):
  cost, trips = solve_case(case)
  print(cost)
  for trip in trips:
    print(*trip)
  if (i != len(cases)-1):
    print()