class Node:
  def __init__(self, iid):
    self.iid = iid;
    self.neighbours = []

  def add_neighbour(self, node):
    self.neighbours += [node]

  def remove_neighbour(self, node):
    self.neighbours.remove(node)

  def __repr__(self):
    return str(self.iid)

class Graph:
  def __init__(self):
    self.nodes = {}
    self.tnodes = set()
    self.visited = set()
    self.path = []

  def add_edge(self, edge):
    if edge[0] not in self.tnodes:
      self.tnodes.add(edge[0])
      self.nodes[edge[0]] = Node(edge[0])

    if edge[1] not in self.tnodes:
      self.tnodes.add(edge[1])
      self.nodes[edge[1]] = Node(edge[1])

    self.nodes[edge[0]].add_neighbour(self.nodes[edge[1]])
    self.nodes[edge[1]].add_neighbour(self.nodes[edge[0]])

  def remove_edge(self, node, neighbour):
    node.remove_neighbour(neighbour)
    neighbour.remove_neighbour(node)

  def check_parity(self):
    for key in self.nodes.keys():
      if len(self.nodes[key].neighbours) % 2 == 0:
        return False
    return True

  def hierholzer_algorithm(self):
    curr_path = []
    final_path = []

    first = True
    sfirst = True
    curr_node = list(self.nodes.values())[0]
    curr_path.append(curr_node)

    while curr_path:
      self.visited.add(curr_node)
      if curr_node.neighbours:
        if first: first = False
        else:
          curr_path = [curr_node] + curr_path

        next_node = curr_node.neighbours[-1]
        self.remove_edge(curr_node, next_node)

        curr_node = next_node

      else:
        if sfirst:
          curr_path = [curr_node] + curr_path
          sfirst = False
        final_path += [curr_node]

        curr_node = curr_path[-1]
        curr_path = curr_path[:-1]

    self.path = final_path[1:] + [final_path[0]]


  def print_path(self):
    self.hierholzer_algorithm()
    if len(self.visited) == len(self.tnodes): 
      if self.path[0] != self.path[-1]:
        print ("some beads may be lost")
      else:
        for x, y in zip(self.path, self.path[1:]):
          print ("{} {}".format(x,y))
    else:
      print ("some beads may be lost")


def read_input():
  num_cases = int(input().strip())
  cases = []
  for case in range(num_cases):
    graph = Graph()
    num_beads = int(input().strip())
    for bead in range(num_beads):
      edge = [int(x) for x in input().strip().split()]
      graph.add_edge(edge)
    cases += [graph]

  return cases


cases = read_input()

for i, case in enumerate(cases):
  print ("Case #{}".format(i+1))
  if not case.check_parity():
    print ("some beads may be lost")
  else:
    case.print_path()
  print()
