class Graph:

  def __init__(self, num_nodes, node_positions):
    self.num_nodes = num_nodes
    self.node_positions = node_positions
    self.edges = [[0] * self.num_nodes for i in range(self.num_nodes)]
    self.build_edges()


  def build_edges(self):
    seen = set()
    for i in range(self.num_nodes):
      for j in range(i+1, self.num_nodes):
        x1, y1 = self.node_positions[i]
        x2, y2 = self.node_positions[j]
        weight = (((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1))) ** (0.5)
        self.edges[i][j] = weight
        self.edges[j][i] = weight

  def getCost(self, parent): 
      cost = 0
      for i in range(1,self.num_nodes): 
        cost += self.edges[parent[i]][ i ]
      return cost

  def findMin(self, keys, visited):
    minv = 2**31
    min_ind = -1
    for i in range(len(keys)):
      if keys[i] < minv and visited[i]==False:
        minv = keys[i]
        min_ind = i
    return min_ind

  def prim_msp(self):
    visited = [False]*self.num_nodes
    keys = [2**31]*self.num_nodes
    parent = [None]*self.num_nodes
    keys[0] = 0
    cost = 0

    for i in range(self.num_nodes):

      u = self.findMin(keys, visited)
      visited[u] = True

      for j in range(self.num_nodes):
        if self.edges[u][j] > 0 and visited[j] == False and keys[j] > self.edges[u][j]:
          keys[j] = self.edges[u][j]
          parent[j] = u
          cost += self.edges[u][j]

    return self.getCost(parent)

def read_input():
  cases = []
  try:
    num_cases = int(input())
    input()
    for i in range(num_cases):
      num_nodes = int(input())
      node_positions = []
      for j in range(num_nodes):
        node_positions += [[float(x) for x in input().split()]]
      cases += [Graph(num_nodes, node_positions)]

      input()
  except EOFError: pass
  return cases


cases = read_input()
for i,case in enumerate(cases):
  print ("{:.2f}".format(case.prim_msp()))
  if i < len(cases)-1:
    print ()
