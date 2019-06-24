inf = 2**31

def australian_voting(votes):
  req_votes = len(votes)/2
  max_votes = 0
  min_votes = inf
  max_candidate = 0
  while max_votes <= req_votes:
    # Count 1st choice
    max_votes = 0
    min_votes = inf
    cand_votes = {x:0 for x in votes[0]}
    for vote in votes:
      cand_votes[vote[0]] += 1

    # Vote is tied
    if len(set(cand_votes.values()))==1:
      return sorted(cand_votes.keys())

    for key in cand_votes.keys():
      if cand_votes[key] > max_votes:
        max_votes = cand_votes[key]
        max_candidate = [key]
      if cand_votes[key] < min_votes: 
        min_votes = cand_votes[key]

    # Remove weakest candidates
    weakest_candidates = []
    for key in cand_votes.keys():
      if cand_votes[key] == min_votes: weakest_candidates += [key]

    for cand in weakest_candidates:
      for vote in votes:
        vote.remove(cand)

  return max_candidate    

def read_input():
  num_cases = int(input().strip())

  cases = []

  input()
  
  for i in range(num_cases):
    num_candidates = int(input().strip())

    candidates = []
    for j in range(num_candidates):
      candidates += [input().strip()]

    votes = []
    while True:
      try:
        line = input().strip()
        if not line:
          break
        votes += [[int(x) for x in line.split()]]
      except EOFError: break

    cases += [[candidates, votes]]

  return cases

cases = read_input()
for i, case in enumerate(cases):
  candidates = australian_voting(case[1])
  for cand in candidates:
    print (case[0][cand-1])
  if i < len(cases)-1: print()
