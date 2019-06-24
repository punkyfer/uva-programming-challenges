def count_days(num_days, hartal_coeffs):
  days_lost = 0
  day = 0
  for x in range(1, num_days+1):
    if day != 5 and day != 6:
      for coeff in hartal_coeffs:
        if x % coeff == 0:
          days_lost += 1
          break
    if day < 6: day += 1
    else: day = 0
  return days_lost

def read_input():
  num_cases = int(input().strip())

  cases = []
  for i in range(num_cases):
    num_days = int(input().strip())
    num_parties = int(input().strip())
    hartal_coeffs = []
    for j in range(num_parties):
      hartal_coeffs += [int(input().strip())]

    cases += [[num_days, hartal_coeffs]]

  return cases


cases = read_input()
for case in cases:
  print (count_days(case[0], case[1]))