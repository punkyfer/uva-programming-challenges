import math

def heron_area(a, b, c, p):
  return math.sqrt(p*(p-a)*(p-b)*(p-c))

def in_radius(a, p):
  return a/p

def perimeter(a, b, c):
  return (a+b+c)/2

def read_input():
  cases = []
  try:
    while(True):
      aux_line = input().strip()
      a, b, c = (float(x) for x in aux_line.split())
      p = perimeter(a, b, c)
      area = heron_area(a,b,c,p)
      if a==0 or b==0 or c==0:
        area, p = 0, 1
      inradius = round(in_radius(area, p), 3)
      inradius_str = str(inradius)
      while len(inradius_str.split(".")[1])<3:
        inradius_str += '0'
      print ("The radius of the round table is: {}".format(inradius_str))

  except EOFError:
    pass
  
read_input()