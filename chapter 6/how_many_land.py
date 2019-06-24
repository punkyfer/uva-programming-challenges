from decimal import *

def read_input():
    cases = []
    try:
        aux_line = int(input().strip())
        for x in range(aux_line):
            aux_line = input().strip()
            cases.append(int(aux_line))
    except EOFError:
        pass
    return cases


def count_land(n):
  t_v = Decimal(n) / 24 * (Decimal(n) ** 3 - 6 * Decimal(n) ** 2 + 23 * n - 18) + 1
  return round( t_v )

getcontext().prec = 64
cases = read_input()

for case in cases:
  print (count_land(case))