def read_input():
  cases = []
  while True:
    n = int(input())
    if n==0:
      break
    case = []
    for i in range(n*2):
      case += [[int(x) for x in input().split()]]
    cases += [[n, case]]

  return cases


def brute_force(n,points):
  l, r = 0, 0
  for i in range(2*n):
    if points[i][0] > 0:
      l += 1
    elif points[i][0] < 0:
      r += 1
  if l==n and r==n:
    return (1,0)
  for a in range(0, 501):
    for b in range(-500, 501):
      l, r = 0, 0
      for i in range(2*n):
        t = a*points[i][0] + b*points[i][1]
        if t > 0:
          l += 1
        elif t < 0:
          r += 1
      if l==n and r==n:
        return (a,b)
  return False


cases = read_input()

for case in cases:
  n, points = case[0], case[1]
  res = brute_force(n, points)
  if res:
    print (str(res)[1:-1].replace(',',''))