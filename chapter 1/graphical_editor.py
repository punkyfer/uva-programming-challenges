def I(m,n):
  img = []
  for x in range(n):
    img += [['O'] * m]
  return img

def C(img):
  for r in range(len(img)):
    for c in range(len(img[r])):
      if img[r][c] != 'O': img[r][c] = 'O'

def L(img, x, y, c):
  img[y][x] = c

def V(img, x, y1, y2, c):
  if y2>y1:
    for i in range((y2-y1)+1):
      img[y1+i][x] = c
  else:
    for i in range((y1-y2)+1):
      img[y2+i][x] = c

def H(img, x1, x2, y, c):
  if x2>x1:
    for i in range((x2-x1)+1):
      img[y][x1+i] = c
  else:
    for i in range((x1-x2)+1):
      img[y][x2+i] = c

def K(img, x1, y1, x2, y2, c):
  if x2 > x1:
    for x in range((x2-x1)+1):
      V(img, x1+x, y1, y2, c)
  else:
    for x in range((x1-x2)+1):
      V(img, x2+x, y1, y2, c)

def F(img, x, y, c):
  og = img[y][x]
  img[y][x] = c
  if og == img[y][x]: return
  if y+1 < len(img) and img[y+1][x] == og: F(img, x, y+1, c)
  if y-1 >= 0 and img[y-1][x] == og: F(img, x, y-1, c)
  if x+1 < len(img[0]) and img[y][x+1] == og: F(img, x+1, y, c)
  if x-1 >= 0 and img[y][x-1] == og: F(img, x-1, y, c)

def S(img, name):
  print(name)
  for row in img:
    print (*row, sep="")


def read_input():
  img = []
  while True:
    aux = input().strip().split()
    if aux[0] == "I": img = I(int(aux[1]), int(aux[2]))
    elif aux[0] == "C": C(img)
    elif aux[0] == "L": L(img, int(aux[1])-1, int(aux[2])-1, aux[3])
    elif aux[0] == "V": V(img, int(aux[1])-1, int(aux[2])-1, int(aux[3])-1, aux[4])
    elif aux[0] == "H": H(img, int(aux[1])-1, int(aux[2])-1, int(aux[3])-1, aux[4])
    elif aux[0] == "K": K(img, int(aux[1])-1, int(aux[2])-1, int(aux[3])-1, int(aux[4])-1, aux[5])
    elif aux[0] == "F": F(img, int(aux[1])-1, int(aux[2])-1, aux[3])
    elif aux[0] == "S": S(img, aux[1])
    elif aux[0] == "X": break

read_input()