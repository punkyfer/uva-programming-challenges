class Elephant:

  def __init__(self, eid, weight, iq):
    self.id = eid
    self.weight = weight
    self.iq = iq

  def __lt__(self, other):
    if self.weight > other.weight: return False
    elif self.weight == other.weight: return self.iq > other.iq
    else: return True

  def __str__(self):
    return "{}: W({}), IQ({})".format(self.id, self.weight, self.iq)

  def __repr__(self):
    return str(self.id)

def read_input():
  elephants = []
  eid = 0
  while True:
    try:
      weight, iq = (int(x) for x in input().split())
      elephants += [Elephant(eid, weight, iq)]
      eid += 1
    except EOFError:
      break
  return elephants


def memoized_dp(elephants):
  elephants.sort(reverse=True)
  maxv, maxi = 0, -1
  mem = [1]*len(elephants)
  #mem += [-1]
  #mem += [-1]*(20-len(elephants))
  mempath = [-1]*len(elephants)

  for i in range(len(elephants)):
    for j in range(i+1, len(elephants)):
      if elephants[j].weight < elephants[i].weight and elephants[j].iq > elephants[i].iq and mem[j]<mem[i]+1:
        mem[j] = mem[i] + 1
        mempath[j] = i
        if mem[j] > maxv:
          maxi = j
          maxv = mem[j]
  
  path = []
  while maxi >= 0:
    path += [elephants[maxi].id]
    maxi = mempath[maxi]

  return path


elephants = read_input()
path = memoized_dp(elephants)

print (len(path))
for x in path:
  print (x+1)