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

def get_path(dp, num_turtles):
  path = []
  f=0
  for i in range(1, num_turtles):
    for j in range(i):
      if dp[i][j]<2**31:
        f = max(f,j)
        if f>0:
          path.append(f)
  return path

def recursive_dp(turtles):
  num_turtles = len(turtles)
  dp = [[2**31 for j in range(n)] for n in range(num_turtles)]
  dp[0] = [0]
  for i in range(num_turtles):
    dp[i][0] = 0
    for j in range(i):
      if dp[i-1][j-1]+turtles[i].weight <= turtles[i].strength:
        dp[i][j] = min(dp[i][j] , dp[i-1][j-1] + turtles[i].weight)

  #print (dp)
  print (len(dp[-1]))

def rec_dp(turtles):
  dp = [2**31 for j in range(5607)]
  dp[0] = 0
  num_turtles = len(turtles)
  maxTurtles = 0

  for i in range(num_turtles):
    for j in range(i):
      if turtles[i].strength >= dp[j] + turtles[i].weight:
        if turtles[i].weight + dp[j-1] < dp[j]:
          dp[j] = turtles[i].weight + dp[j-1]
          maxTurtles = max(maxTurtles, j-1)

  return maxTurtles

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

#for turtle in turtles:
#  print (turtle.weight, turtle.strength)

#recursive_dp(turtles)
print (rec_dp_2(turtles))