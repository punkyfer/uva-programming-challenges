def read_input():
  cases = []
  try:
    aux_line = input().strip()
    while (aux_line != None):
      cases.append(int(aux_line))
      aux_line = input().strip()
  except EOFError:
    pass
  return cases

def solve_case(n):
  T = [0 for x in range(n+3)]
  T[0] = 1
  T[1] = 2
  T[2] = 5
  for i in range(3,n+1):
    T[i] = T[i] * 4 + T[i-1] + T[i-2] + T[i-3] + T[i-1]

  return T[n]


cases = read_input()
for case in cases:
  print(solve_case(case))