import networkx as nx
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def read_input():
    cases = []
    try:
      while(True):
        aux_line = input().strip()

        while aux_line == "":
          if town_array not in cases:
            cases.append(town_array)
          aux_line = input().strip()
        num_towns, num_town_pairs = (int(x) for x in aux_line.split(" "))
        if num_towns == 0 and num_town_pairs == 0:
          if town_array not in cases: cases.append(town_array)
          return cases
          
        if num_town_pairs == 0 and num_towns != 0:
          town_array = [num_towns]
        else:
          town_array = [[0 for x in range(num_towns)] for y in range(num_towns)]
          for x in range(num_towns):
            town_array[x][x] = 1
          for x in range(num_town_pairs):
            town1, town2 = (int(x) for x in input().strip().split(" ") if x!="")
            town_array[town1-1][town2-1] = 1
            town_array[town2-1][town1-1] = 1 
    except EOFError:
      pass
 
A  =  [[0.000000,  0.0000000,  0.0000000,  0.0000000,  0.05119703, 1.3431599],
     [0.000000,  0.0000000, -0.6088082,  0.4016954,  0.00000000, 0.6132168],
       [0.000000, -0.6088082,  0.0000000,  0.0000000, -0.63295415, 0.0000000],
       [0.000000,  0.4016954,  0.0000000,  0.0000000, -0.29831267, 0.0000000],
       [0.051197,  0.0000000, -0.6329541, -0.2983127,  0.00000000, 0.1562458],
       [1.343159,  0.6132168,  0.0000000,  0.0000000,  0.15624584, 0.0000000]]

puzzles = read_input()

puzzle = puzzles[2]

G = nx.from_numpy_matrix(np.array(puzzle)) 
nx.draw(G, with_labels=True)
plt.savefig("Graph.png", format="PNG")