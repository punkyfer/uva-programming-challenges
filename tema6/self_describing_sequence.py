def read_input():
  cases = []
  try:
    aux_line = input().strip()
    while (aux_line != None):
      input_int = int(aux_line)
      if input_int == 0:
        break
      else:
        cases.append(input_int)
      aux_line = input().strip()
  except EOFError:
    pass
  return cases

def gen_table(n = 2000000000):
  g_t = [0, 1, 3, 5]
  temp = [2]
  end_val = 5
  i = 3
  while end_val < n:
    mult = temp.pop(0)
    for x in range(mult):
      end_val += i
      g_t += [end_val]
    temp += [i] * mult
    i += 1

  return g_t

def binary_search(n, table):
  begin, end = 0, len(table)-1
  done = False
  mod = 0
  while not done and begin <= end:
    mid = (begin + end)//2
    if n > table[mid]:
      if n <= table[mid+1]:
        mod = 1
        done = True
      else:
        begin = mid + 1
    elif n <= table[mid]:
      if n > table[mid-1]:
        mod = 0
        done = True
      else:
        end = mid - 1

  return mid + mod

t_t = gen_table()

cases = read_input()
for case in cases:
  print(binary_search(case, t_t))


