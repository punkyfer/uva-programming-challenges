def shuffle_cards(cards, shuffle): 
  new_cards = [x for x in range(1,53)]

  for j, i in enumerate(shuffle):
    new_cards[j]=cards[i]

  return new_cards

def read_input():
  num_cases = int(input().strip())

  cases = []
  input()
  for i in range(num_cases):
    num_shuffles = int(input().strip())

    shuffles = []

    for j in range(num_shuffles):
      shuffle = []
      while len(shuffle)<52: shuffle += [int(x)-1 for x in input().strip().split()] 
      shuffles += [shuffle]

    shuffle_order = []

    while True:
      try:
        line = input().strip()
        if not line:
          break
        shuffle_order += [int(line)-1]
      except EOFError: break

    cases += [[shuffles, shuffle_order]]

  return cases


cases = read_input()
for i, case in enumerate(cases):
  cards = [x for x in range(1,53)]
  for so in case[1]:
    cards = shuffle_cards(cards, case[0][so])

  for num in cards:
    if num <= 13: 
      suit = "Clubs"
      nnum = num
    elif num <= 26: 
      suit = "Diamonds"
      nnum = num - 13
    elif num <= 39: 
      suit = "Hearts"
      nnum = num - 26
    elif num <= 52: 
      suit = "Spades"
      nnum = num - 39

    if nnum == 10: value = "Jack"
    elif nnum == 11: value = "Queen"
    elif nnum == 12: value = "King"
    elif nnum == 13: value = "Ace"
    else: value = nnum+1

    print ("{} of {}".format(value, suit))
  if i < len(cases)-1: print()