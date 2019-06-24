def read_input():
    cases = []
    try:
        aux_line = input().strip()
        while (aux_line != None):
            n_rows, n_bishops = int(aux_line.split()[0]), int(aux_line.split()[1])
            if n_rows == 0 and n_bishops == 0:
              break
            else:
              cases.append([n_rows, n_bishops])
            aux_line = input().strip()
    except EOFError:
        pass
    return cases

def split_board(n_rows):
  w_b = [0 for x in range(9)]
  b_b = [0 for x in range(9)]
  for i in range(1, n_rows+1):
    w_b[i] = i if i % 2 != 0 else w_b[i-1]
  for i in range(1, n_rows):
    b_b[i] = i + 1 if i % 2 != 0 else b_b[i-1]
  return w_b, b_b

def solve_bishops(n_rows, n_bishops):
  w_b, b_b = split_board(n_rows)
  w_c = [[0 for x in range(65)] for x in range(9)]
  b_c = [[0 for x in range(65)] for x in range(9)]

  for i in range(n_rows+1):
    w_c[i][0] = 1
  for i in range(1, n_rows+1):
    for j in range(1, n_bishops+1):
      if j > i:
        break
      else:
        w_c[i][j] = w_c[i-1][j] + w_c[i-1][j-1]*(w_b[i] - j + 1)

  for i in range(n_rows):
    b_c[i][0] = 1
  for i in range(1, n_rows):
    for j in range(1, n_bishops+1):
      if j > i:
        break
      else:
        b_c[i][j] = b_c[i-1][j] + b_c[i-1][j-1]*(b_b[i] - j + 1)

  res = 0
  for i in range(n_bishops+1):
    res += w_c[n_rows][i] * b_c[n_rows-1][n_bishops-i]
  return res

cases = read_input()

for case in cases:
  print (solve_bishops(case[0], case[1]))
