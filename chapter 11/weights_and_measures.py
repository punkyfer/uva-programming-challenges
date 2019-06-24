class Turtle():
  def __init__(self, weight, strength):
    self.weight = weight
    self.strength = strength

  def __lt__(self, other):
    if self.strength==other.strength: return self.weight < other.weight
    return self.strength < other.strength

def read_input():
  turtles = []
  try:
    while(True):
      aux_line = input().strip()
      weight, strength = int(aux_line.split()[0]), int(aux_line.split()[1])
      turtles.append(Turtle(weight, strength))
  except EOFError:
    pass
  return turtles

def rec_dp_2(turtles):
  dp = [2**31 for j in range(5607)]
  dp[0] = 0
  num_turtles = len(turtles)
  maxTurtles = 0

  for i in range(num_turtles):
    for j in range(maxTurtles, -1, -1):
      if turtles[i].strength >= dp[j] + turtles[i].weight and dp[j]+turtles[i].weight < dp[j+1]:
        dp[j+1] = turtles[i].weight + dp[j]
        maxTurtles = max(maxTurtles, j+1)

  return maxTurtles

turtles = read_input()

turtles.sort()

print (rec_dp_2(turtles))