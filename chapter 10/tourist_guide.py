class Vertex:

  def __init__(self,cid, name):
    self.name = name
    self.cid = cid
    self.num = 0
    self.low = 0
    self.visited = False
    self.parent = None
    self.adjacent = []
    self.children = []

  def add_connection(self, v):
    self.adjacent += [v]

  def __eq__(self, other):
    if (isinstance(other, Vertex)):
      return self.__hash__() == other.__hash__()
    return False 

  def __repr__(self):
    return self.name

  def __hash__(self):
    return hash(repr(self))

  def __lt__(self, other):
    if len(self.name) < len(other.name):
      return True
    elif len(self.name) == len(other.name):
      min_name = min(self.name, other.name)
      if self.name == min_name:
        return True
    return False

def read_input():
    cases = []
    try:
      aux_line = int(input().strip())
      while(aux_line != 0):
        Graph = {}
        root = None
        for x in range(aux_line):
          name = input().strip()
          Graph[name] = Vertex(x, name)
          if x == 0:
            root = Graph[name]
        num_connections = int(input().strip())
        for y in range(num_connections):
          c1, c2 = input().strip().split()
          city1, city2 = Graph[c1], Graph[c2]
          city1.add_connection(city2)
          city2.add_connection(city1)

        cases += [[Graph, root]]
        aux_line = int(input().strip())

    except EOFError:
        pass
    return cases

def findArticulationPoints(vertex, art_points):
  global counter
  global visited
  visited.add(vertex)
  vertex.visited = True
  counter += 1
  vertex.num = counter
  vertex.low = counter
  for avertex in vertex.adjacent:
    if not avertex.visited:
      avertex.parent = vertex
      vertex.children += [avertex]
      findArticulationPoints(avertex, art_points)
      if avertex.low >= vertex.num:
        if vertex.parent != None:
          art_points.add(vertex)
      vertex.low = min(vertex.low, avertex.low);
    else:
      if vertex.parent != avertex:
        vertex.low = min(vertex.low, avertex.num)
  if vertex.parent == None and len(vertex.children) > 1:
    art_points.add(vertex)


cases = read_input()
for i,case in enumerate(cases):
  counter = 0
  art_points = set()
  visited = set()
  findArticulationPoints(case[1], art_points)
  while len(visited) < len(case[0]):
    root = None
    aux = 0
    for vkey in case[0].keys():
      if not case[0][vkey].visited:
        if len(case[0][vkey].adjacent) == 0:
          visited.add(len(visited))
        if len(case[0][vkey].adjacent) > aux:
          aux = len(case[0][vkey].adjacent)
          root = case[0][vkey]
    if root == None:
      break
    else:
      findArticulationPoints(root, art_points)
  print ("City map #{}: {} camera(s) found".format(i+1, len(art_points)))
  for city in sorted(art_points):
    print (city)
  if i < len(cases) -1:
    print()