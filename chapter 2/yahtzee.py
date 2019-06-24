import copy

class Yahtzee:
  
  def __init__(self, game):
    self.rounds = [x for x in range(13)]
    self.score_matrix = self.get_score_matrix(game)
    self.temp_matrix = []
    self.choices = [None]
    self.inf = 2**31
    self.mlen = 13
    self.sols = {}

  def get_score_matrix(self, game):
    score_matrix = []
    for tthrow in game:
      dthrow = sorted(tthrow)
      ones = 0
      twos = 0
      threes = 0
      fours = 0
      fives = 0
      sixes = 0
      chance = 0
      three_of_a_kind = 0
      four_of_a_kind = 0
      five_of_a_kind = 0
      short_straight = 0
      long_straight = 0
      full_house = 0
      for dnum in dthrow:
        if dnum == 1: ones += 1
        elif dnum == 2: twos += 2
        elif dnum == 3: threes += 3
        elif dnum == 4: fours += 4
        elif dnum == 5: fives += 5
        elif dnum == 6: sixes += 6
        chance += dnum

      dtset = list(set(dthrow))
      for n in dtset:
        ncount = dthrow.count(n)
        if ncount == 3: three_of_a_kind = chance
        if ncount == 4: four_of_a_kind = chance
        if ncount == 5: five_of_a_kind = 50    

      if dthrow[1:]==[1,2,3,4] or dthrow[1:]==[2,3,4,5] or dthrow[1:]==[3,4,5,6]:
        short_straight = 25

      if dthrow[:-1]==[1,2,3,4] or dthrow[:-1]==[2,3,4,5] or dthrow[:-1]==[3,4,5,6]:
        short_straight = 25

      if dthrow==[1,2,3,4,5] or dthrow==[2,3,4,5,6]:
        long_straight = 35

      if len(dtset) == 2:
        if dthrow.count(dtset[0]) == 2 and dthrow.count(dtset[1])==3:
          full_house = 40
        if dthrow.count(dtset[1]) == 2 and dthrow.count(dtset[0])==3:
          full_house = 40
      score_matrix += [[ones, twos, threes, fours, fives, sixes, chance, three_of_a_kind, four_of_a_kind,
        five_of_a_kind, short_straight, long_straight, full_house]]

    return score_matrix

  def all_zeros_marked(self, matrix, marked_rows, marked_cols):
    for i, row in enumerate(matrix):
      for j, elem in enumerate(row):
        if elem == 0:
          if marked_rows[i]!=1 and marked_cols[j]!=1:
            return False
    return True

  def dp_min_lines(self, curr_i, matrix, marked_rows, marked_cols):
    if curr_i == self.mlen:
      if self.all_zeros_marked(matrix, marked_rows, marked_cols):
        self.sols[marked_rows.count(1)+marked_cols.count(1)] = (marked_rows, marked_cols)
        return 0
      else:
        return self.inf

    zero_c = False
    for i in range(self.mlen):
      if matrix[i][curr_i] == 0 and marked_rows[curr_i] == 0:
        zero_c = True

    zero_r = False
    for i in range(self.mlen):
      if matrix[curr_i][i] == 0 and marked_cols[curr_i] == 0:
        zero_r = True


    dp_vals = [self.dp_min_lines(curr_i+1, matrix, marked_rows, marked_cols),
               self.dp_min_lines(curr_i+1, matrix, marked_rows[:curr_i]+[1]+marked_rows[curr_i+1:], marked_cols)+1 if zero_r else self.inf,
               self.dp_min_lines(curr_i+1, matrix, marked_rows, marked_cols[:curr_i]+[1]+marked_cols[curr_i+1:])+1 if zero_c else self.inf]
    
    min_index = dp_vals.index(min(dp_vals))
    return min(dp_vals)

  def subtract_matrix_to_max(self):
    max_v = 0
    for row in self.score_matrix:
      for elem in row:
        if elem > max_v: max_v = elem
    
    matrix = []
    for row in self.score_matrix:
      new_row = []
      for elem in row:
        new_row += [max_v-elem]
      matrix += [new_row]
    return matrix
    
  def subtract_min_rows(self, matrix):
    for row in matrix:
      min_v = min(row)
      for i, elem in enumerate(row):
        row[i] = elem-min_v

  def subtract_min_cols(self, matrix):
    for col in range(self.mlen):
      min_v = self.inf
      for row in matrix:
        if row[col] < min_v: min_v = row[col]

      for row in matrix:
        row[col] = row[col]-min_v

  def subtract_min_unmarked(self, matrix, marked_rows, marked_cols):
    min_v = self.inf
    for i, row in enumerate(matrix):
      if marked_rows[i] == 0:
        for j, elem in enumerate(row):
          if marked_cols[j] == 0:
            if elem < min_v: min_v = elem

    for i in range(self.mlen):
      for j in range(self.mlen):
        if marked_rows[i] == 0:
          matrix[i][j] -= min_v
        if marked_cols[j] == 1:
          matrix[i][j] += min_v

  def mark_matrix(self, matrix, row, col):
    new_matrix = copy.deepcopy(matrix)
    for i, elem in enumerate(new_matrix[row]):
      if elem==0 and i!=col:
        new_matrix[row][i]=self.inf

    for i in range(self.mlen):
      if matrix[i][col]==0 and i!=row:
        new_matrix[i][col]=self.inf

    return new_matrix


  def find_path(self, curr_i, matrix, chosen_cat):
    if curr_i == self.mlen:
      for row in matrix:
        if row.count(0) != 1:
          return False
      return True
    for j, elem in enumerate(matrix[curr_i]):
      if elem == 0:
        chosen_cat[j] = curr_i
        mmatrix = self.mark_matrix(matrix, curr_i, j)
        path = self.find_path(curr_i+1, mmatrix, chosen_cat)
        if path: return True
    return False

  def test_munkres(self):
    self.temp_matrix = [[108,125,150],[150,135,175],[122,148,250]]
    self.mlen = 3

    print ("Original Matrix")
    for row in self.temp_matrix:
      print (row)
    print ()
    
    #Step 1
    self.subtract_min_rows(self.temp_matrix)

    print ("Step 1: Subtract smallest from each row")
    for row in self.temp_matrix:
      print (row)
    print ()

    #Step 2
    self.subtract_min_cols(self.temp_matrix)

    print ("Step 1: Subtract smallest from each column")
    for row in self.temp_matrix:
      print (row)
    print ()


    marked_rows = [0]*self.mlen
    marked_cols = [0]*self.mlen
    min_lines = self.dp_min_lines(0, self.temp_matrix, marked_rows, marked_cols)
    marked_rows, marked_cols = self.sols[min_lines]

    print ("Step 3: Count min lines")  
    print ("min_ines = ", min_lines)
    print ("Rows: ", marked_rows)
    print ("Cols: ", marked_cols)
    for row in self.temp_matrix:
      print (row)
    print()

    runOnce = False
    while min_lines < self.mlen:
      self.subtract_min_unmarked(self.temp_matrix, marked_rows, marked_cols)
      print ("Step 5: Subtract smallest from unmarked cells")
      for row in self.temp_matrix:
        print (row)
      print ()

      marked_rows = [0]*self.mlen
      marked_cols = [0]*self.mlen
      min_lines = self.dp_min_lines(0, self.temp_matrix, marked_rows, marked_cols)
      marked_rows, marked_cols = self.sols[min_lines]

      print ("Step 3: Count min lines")  
      print ("min_ines = ", min_lines)
      print ("Rows: ", marked_rows)
      print ("Cols: ", marked_cols)
      for row in self.temp_matrix:
        print (row)
      print ()

      if runOnce: break

    chosen_categories = [-1]*self.mlen
    path_found = self.find_path(0, self.temp_matrix, chosen_categories)

    print ("Step 4: min_lines = mlen -> Algorithm Finished")
    print ("Path Found = ", path_found)
    print (chosen_categories)

  def calculate_score(self, chosen_categories):
    score_array = []
    bonus_score = 0
    total_score = 0
    for cat, row in enumerate(chosen_categories):
      if cat < 6: bonus_score += self.score_matrix[row][cat]
      score_array += [self.score_matrix[row][cat]]
      total_score += self.score_matrix[row][cat]

    if bonus_score >= 63: 
      bonus_score = 35
      total_score += 35
    else: bonus_score = 0

    score_array += [bonus_score, total_score]

    return score_array


  def get_solution(self):
    # Subtract each element of matrix to max, so we find the maximal elements
    self.temp_matrix = self.subtract_matrix_to_max()

    # 1 - Subtract the smallest value in each row to the whole row
    self.subtract_min_rows(self.temp_matrix)

    # 2 - Subtract the smallest value in each column to the whole column
    self.subtract_min_cols(self.temp_matrix)

    # 3 - Draw lines through the row and columns that have the 0 entries such that 
    #     the fewest lines possible are drawn.
    marked_cols = [0]*self.mlen
    marked_rows = [0]*self.mlen
    min_lines = self.dp_min_lines(0, self.temp_matrix, marked_rows, marked_cols)
    marked_rows, marked_cols = self.sols[min_lines]

    while min_lines < self.mlen:
      # 5 - Find the smallest entry not covered by any line. Subtract this entry from each
      #     row that isn’t crossed out, and then add it to each column that is crossed out.
      self.subtract_min_unmarked(self.temp_matrix, marked_rows, marked_cols)

      # 3 - Draw lines through the row and columns that have the 0 entries such that 
      #     the fewest lines possible are drawn.
      marked_cols = [0]*self.mlen
      marked_rows = [0]*self.mlen
      min_lines = self.dp_min_lines(0, self.temp_matrix, marked_rows, marked_cols)
      marked_rows, marked_cols = self.sols[min_lines]

    # 4 - there are nn lines drawn, an optimal assignment of zeros is possible, the algorithm is finished
    chosen_categories = [-1]*self.mlen
    path_found = self.find_path(0, self.temp_matrix, chosen_categories)

    score_array = self.calculate_score(chosen_categories)
    return score_array

def read_input():

  try:
    while(True):
      game = []
      for i in range(13):
        game += [[int(x) for x in input().split()]]

      yt = Yahtzee(game)
      #yt.test_munkres()
      score = yt.get_solution()
      print (*score)

  except EOFError: pass


read_input()