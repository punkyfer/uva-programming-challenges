import math

def read_input():
  cases = []
  try:
    while(True):
      cases.append(float(input().strip()))
  except EOFError:
    pass
  return cases


def format_num(num):
  str_num = str(round(num,3))
  while len(str_num.split(".")[1]) < 3:
    str_num += "0"
  return str_num

nums = read_input()

for num in nums:
  area = num**2 # X + 4Y + 4Z
  y_2z = area-(math.pi*area)/4 # Y + 2Z
  z = area*(1-(math.pi/6)-(math.sqrt(3)/4))
  y = y_2z - 2*z
  x = area - 4*y - 4*z
  print ("{} {} {}".format(format_num(x),format_num(4*y),format_num(4*z)))