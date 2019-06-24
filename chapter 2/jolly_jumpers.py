def jolly_jumper(n, seq):
  goal = [x+1 for x in range(n-1)]

  difs = []
  for i, e in enumerate(seq[:-1]):
    difs += [abs(e-seq[i+1])]

  if sorted(difs) == goal: return True

  return False

def read_input():
  try:
    while True:
      case = [int(x) for x in input().split()]

      if jolly_jumper(case[0], case[1:]): print("Jolly")
      else: print("Not jolly") 

  except EOFError: pass

read_input()