def read_input():
  cases = []
  try:
    while(True):
      cases.append(int(input().strip()))
  except EOFError:
    pass
  return cases

def find_ring_num(cell_num):
  r, k = 0, 1
  while (cell_num > k):
    r+=1
    k += r*6
  return k, r

def bee_backtracking(cell_num, ring_num, last_num):
  x, y = ring_num, 0
  n, k = cell_num, last_num
  while x!=-y and k!=n:
    # UP
    y -= 1
    k -= 1
  while x!=0 and k!=n:
    # UP-LEFT
    x-= 1
    k -= 1
  while y!=0 and k!=n:
    # DOWN-LEFT
    y += 1
    x -= 1
    k -= 1
  while x!=-y and k!=n:
    # DOWN
    y += 1
    k -= 1
  while x!=0 and k!=n:
    # DOWN-RIGHT
    x += 1
    k -= 1
  while y!=0 and k!=n:
    # UP-RIGHT
    x += 1
    y -= 1
    k -= 1
  return (x, y)


cases = read_input()

for num in cases:
  last_num, ring_num = find_ring_num(num)
  x, y = bee_backtracking(num, ring_num, last_num)
  print ("{} {}".format(x,y))