def iter_dp(cuts):
  n = len(cuts)
  mem = {}
  for k in range(0,n):
    for i in range(n-1-k):
      j = i+1+k
      if k==0: 
        mem[(i,j)] = 0
      else:
        mem[(i,j)] = cuts[j] - cuts[i] + min([mem[(i,l)] + mem[(l,j)] for l in range(i+1,j)])

  return mem[(0,n-1)]

def read_input():
  cases = []
  while True:
    l = int(input())
    if l == 0:
      break
    n = int(input())
    cuts = [int(x) for x in input().split()]
    cuts = [0]+cuts+[l]
    
    print ("The minimum cutting is {}.".format(iter_dp(cuts)))


read_input()