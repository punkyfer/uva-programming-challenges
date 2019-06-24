import math

def read_input():
  cases = []
  try:
    while (True):
      numbers = [int(x) for x in input().strip().split()]
      cases.append(numbers)
  except EOFError:
    pass
  return cases

def get_powers(n, p):
  res = 0
  power = p
  while (power <= n):
    res += n/power
    power *= p

  return res

def sieve(n):
  spf[1] = 1
  for i in range(2, n):
    spf[i] = i

  for i in range(4, n, 2):
    spf[i] = 2

  for i in range(3, math.ceil(math.sqrt(n))):
    if spf[i] == i:
      for j in range(i * i, n, i):
        if spf[j] == j:
          spf[j] = i


def getFactors(n):
  #ret = []
  dic = {}
  x = n
  while (x != 1):
    try:
      dic[spf[x]] += 1
    except:
      dic[spf[x]] = 1
    #ret += [spf[x]]
    x = x // spf[x]

  return dic

def primeFactors(x):
  n = x
  ret = {}
  while n%2 == 0:
    try:
      ret[2] += 1
    except:
      ret[2] = 1
    n = n / 2

  for i in range(3, int(math.sqrt(n))+1, 2):
    while n % i == 0:
      try:
        ret[i] += 1
      except:
        ret[i] = 1
      n = n / i

  if n > 2:
    try:
      ret[n] += 1
    except:
      ret[n] = 1

  return ret

#mn = 2147483648
#mn = 50000
numbers = read_input()
#spf = [0 for i in range(mn)] 
#sieve(mn)

for (n, m) in numbers:
  #if m>math.factorial(n): div = False
  if m==0: div = True
  elif n==0 and m==1: div = True 
  else:
    """
    if m <= mn:
      factors = getFactors(m)
    else:
      factors = primeFactors(m)
    """
    factors = primeFactors(m)
    div = True
    for factor in factors:
      if get_powers(n, factor) < factors[factor]:
        div = False
        break
  if div:
    print ("{} divides {}!".format(m, n))
  else:
    print ("{} does not divide {}!".format(m, n))