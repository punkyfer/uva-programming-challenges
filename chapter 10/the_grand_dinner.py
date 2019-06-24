def read_input():
    cases = []
    try:
      while(True):
        aux_line = [int(x) for x in input().strip().split()]
        num_teams, num_tables = aux_line[0], aux_line[1]
        if num_teams == num_tables and num_tables == 0:
          break
        else:
          teams = []
          for i,x in enumerate(input().strip().split()):
            teams.append([i+1,int(x)])
          tables = []
          for i,x in enumerate(input().strip().split()):
            tables.append([i+1, int(x)])
          cases += [[teams, tables]]
    except EOFError:
        pass
    return cases

def delete_from_list(olist, ids):
  for i in sorted(ids, reverse=True):
    del(olist[i])

def greedy_search(teams, tables):
  team_tables = [[] for team in teams]+[[]]
  while(len(teams) > 0):
    if len(tables) == 0:
      if len(teams)==1 and teams[0][1] == 0:
        return team_tables
      else:
        return 0
    teams = sorted(teams, key = lambda x: x[1], reverse=True)
    tables = sorted(tables, key = lambda x: x[1], reverse=True)

    for x in range(tables[0][1]):
      if x < len(teams):
        teams[x][1] -= 1
        team_tables[teams[x][0]] += [tables[0][0]]

    ids = []
    for i,team in enumerate(teams):
      if team[1] == 0:
        ids += [i]
    delete_from_list(teams, ids)

    tables.pop(0)

  return team_tables


cases = read_input()
for case in cases:
  if sum([x[1] for x in case[0]]) > sum([x[1] if x[1]<=len(case[0]) else len(case[0])  for x in case[1]]):
    print(0)
  else:
    result = greedy_search(case[0], case[1])
    if result == 0:
      print (0)
    else:
      print(1)
      for team in result[1:]:
        print(' '.join(str(e) for e in team))
