def read_input():
  num_cases = int(input().strip())
  cases = []
  for case in range(num_cases):
    x = input().strip()
    z = input().strip()
    cases += [[x,z]]

  return cases


def memoized_subsequences(x, z):

  mem_arr = [[0 for j in range(len(x)+1)] for i in range(len(z)+1)]
  mem_arr[0] = [1 for j in range(len(x)+1)]

  for i in range(1,len(z)+1):
    for j in range(1, len(x)+1):
      if x[j-1]==z[i-1]: mem_arr[i][j] = mem_arr[i-1][j-1] + mem_arr[i][j-1]
      else: mem_arr[i][j] = mem_arr[i][j-1]

  return mem_arr[len(z)][len(x)]


cases = read_input()

for case in cases:
  print (memoized_subsequences(case[0], case[1]))