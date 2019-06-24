def cround(x):
  nx = x*100

while True:
  numstudents = int(input().strip())

  if numstudents == 0: break

  costs = []
  avg = 0
  for i in range(numstudents):
    cost = float(input().strip())
    avg += cost
    costs += [cost]

  avg = round(avg / numstudents, 2)

  ndif, pdif = 0, 0
  for cost in costs:
    if cost > avg:
      pdif += cost - avg
    else:
      ndif += avg - cost

  if ndif < pdif:
    print ("${:0.2f}".format(ndif))
  else:
    print ("${:0.2f}".format(pdif))
