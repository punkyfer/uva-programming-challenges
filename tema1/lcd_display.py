def print_nums(nums, size):
    # Top Part
    line = ""
    for i, num in enumerate(nums):
      if num in [1, 4]: line += " " + " "*size + " "
      else: line += " " + "-"*size + " "
      if i<len(nums)-1: line += " "
    print (line)
    # Top - Middle
    for x in range(size):
      line = ""
      for i, num in enumerate(nums):
        if num in [0, 4, 8, 9]: line += "|" + " "*size + "|"
        elif num in [1, 2, 3, 7]: line += " " + " "*size + "|" 
        else: line += "|" + " "*size + " " 
        if i<len(nums)-1: line += " "
      print (line)
    # Middle Part
    line = ""
    for i, num in enumerate(nums):
      if num in [0, 1, 7]: line += " " + " "*size + " "
      else: line += " " + "-"*size + " "
      if i<len(nums)-1: line += " "
    print (line)
    # Middle - Bottom
    for x in range(size):
      line = ""
      for i, num in enumerate(nums):
        if num in [0, 6, 8]: line += "|" + " "*size + "|"
        elif num in [1, 3, 4, 5, 7, 9]: line += " " + " "*size + "|"
        else:  line += "|" + " "*size + " "
        if i<len(nums)-1: line += " "
      print (line)
    # Bottom Part
    line = ""
    for i, num in enumerate(nums):
      if num in [0, 2, 3, 5, 6, 8, 9]: line += " " + "-"*size + " "
      else: line += " " + " "*size + " "
      if i<len(nums)-1: line += " "
    print (line)

def read_input():
  while True:
    aux = input().strip().split()
    size = int(aux[0])
    if size==0: break
    nums = []
    for i in aux[1]:
      nums += [int(i)]

    print_nums(nums, size)
    print ()

read_input()