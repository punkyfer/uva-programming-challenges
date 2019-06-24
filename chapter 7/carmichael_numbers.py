def read_input():
  numbers = []
  try:
    while (True):
      number = int(input().strip())
      if number == 0: break
      numbers.append(number)
  except EOFError:
    pass
  return numbers

numbers = read_input()

carmichael_nums = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973]
for number in numbers:
	if number in carmichael_nums:
		print ("The number {} is a Carmichael number.".format(str(number)))
	else:
		print ("{} is normal.".format(str(number)))