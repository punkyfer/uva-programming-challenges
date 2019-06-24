end_board = [["."]*8]*8

def check_pawn(board, y, x, color):
  if color == "black":
    if y+1 < 8:
      if x+1 < 8 and board[y+1][x+1]=="K":
        return True
      if x-1 >= 0 and board[y+1][x-1]=="K":
        return True
  if color == "white":
    if y-1 >= 0:
      if x+1 < 8 and board[y-1][x+1]=="k":
        return True
      if x-1 >= 0 and board[y-1][x-1]=="k":
        return True
  return False

def check_king(board, y, x, color):
  if x+1 < 8: 
    if board[y][x+1]=="K" and color=="black":
      return True
    if board[y][x+1]=="k" and color=="white":
      return True
  if x-1 >= 0:
    if board[y][x-1]=="K" and color=="black":
      return True
    if board[y][x-1]=="k" and color=="white":
      return True
  if y+1 < 8:
    if x-1 >= 0:
      if board[y+1][x-1]=="K" and color=="black": 
        return True
      if board[y+1][x-1]=="k" and color=="white": 
        return True
    if x+1 < 8:
      if board[y+1][x+1]=="K" and color=="black":
        return True
      if board[y+1][x+1]=="k" and color=="white":
        return True
    if board[y+1][x] == "K" and color=="black":
      return True
    if board[y+1][x] == "k" and color=="white":
      return True
  if y-1 >= 0:
    if x-1 >= 0:
      if board[y-1][x-1]=="K" and color=="black": 
        return True
      if board[y-1][x-1]=="k" and color=="white": 
        return True
    if x+1 < 8:
      if board[y-1][x+1]=="K" and color=="black":
        return True
      if board[y-1][x+1]=="k" and color=="white":
        return True
    if board[y-1][x] == "K" and color=="black":
      return True
    if board[y-1][x] == "k" and color=="white":
      return True
  return False

def check_knight(board, y, x, color):
  if y+1 < 8:
    if x-2 >= 0:
      if board[y+1][x-2]=="K" and color=="black": 
        return True
      if board[y+1][x-2]=="k" and color=="white": 
        return True
    if x+2 < 8:
      if board[y+1][x+2]=="K" and color=="black":
        return True
      if board[y+1][x+2]=="k" and color=="white":
        return True
  if y+2 < 8:
    if x-1 >= 0:
      if board[y+2][x-1]=="K" and color=="black": 
        return True
      if board[y+2][x-1]=="k" and color=="white": 
        return True
    if x+1 < 8:
      if board[y+2][x+1]=="K" and color=="black":
        return True
      if board[y+2][x+1]=="k" and color=="white":
        return True
  if y-1 >= 0:
    if x-2 >= 0:
      if board[y-1][x-2]=="K" and color=="black": 
        return True
      if board[y-1][x-2]=="k" and color=="white": 
        return True
    if x+2 < 8:
      if board[y-1][x+2]=="K" and color=="black":
        return True
      if board[y-1][x+2]=="k" and color=="white":
        return True
  if y-2 >= 0:
    if x-1 >= 0:
      if board[y-2][x-1]=="K" and color=="black": 
        return True
      if board[y-2][x-1]=="k" and color=="white": 
        return True
    if x+1 < 8:
      if board[y-2][x+1]=="K" and color=="black":
        return True
      if board[y-2][x+1]=="k" and color=="white":
        return True
  return False

def check_rook(board, y, x, color):
  for i in range(y-1,-1,-1):
    if board[i][x] == "K" and color=="black":
      return True
    if board[i][x] == "k" and color=="white":
      return True
    if board[i][x] != ".": break
  for i in range(y+1,8):
    if board[i][x] == "K" and color=="black":
      return True
    if board[i][x] == "k" and color=="white":
      return True
    if board[i][x] != ".": break
  for j in range(x-1,-1,-1):
    if board[y][j] == "K" and color=="black":
      return True
    if board[y][j] == "k" and color=="white":
      return True
    if board[y][j] != ".": break
  for j in range(x+1,8):
    if board[y][j] == "K" and color=="black":
      return True
    if board[y][j] == "k" and color=="white":
      return True
    if board[y][j] != ".": break
  return False

def check_bishop(board, y, x, color):
  ctr = 1
  for i in range(y-1,-1,-1):
    if x-ctr >= 0:
      if board[i][x-ctr]=="K" and color=="black":
        return True
      if board[i][x-ctr]=="k" and color=="white":
        return True
      if board[i][x-ctr] != ".": break
      ctr += 1
    else: break
  ctr = 1
  for i in range(y-1,-1,-1):
    if x+ctr < 8:
      if board[i][x+ctr]=="K" and color=="black":
        return True
      if board[i][x+ctr]=="k" and color=="white":
        return True
      if board[i][x+ctr] != ".": break
      ctr += 1
    else: break
  ctr = 1
  for i in range(y+1, 8):
    if x-ctr >= 0:
      if board[i][x-ctr]=="K" and color=="black":
        return True
      if board[i][x-ctr]=="k" and color=="white":
        return True
      if board[i][x-ctr] != ".": break
      ctr += 1
    else: break
  ctr = 1
  for i in range(y+1, 8):
    if x+ctr < 8:
      if board[i][x+ctr]=="K" and color=="black":
        return True
      if board[i][x+ctr]=="k" and color=="white":
        return True
      if board[i][x+ctr] != ".": break
      ctr += 1
    else: break
  return False

def check_pieces(board):
  whiteKingcheck = False
  blackKingcheck = False
  for y in range(8):
    for x in range(8):
      if board[y][x] == 'p' and not whiteKingcheck:
        whiteKingcheck = check_pawn(board, y, x, "black")
      if board[y][x] == 'k' and not whiteKingcheck:
        whiteKingcheck = check_king(board, y, x, "black")
      if board[y][x] == 'n' and not whiteKingcheck:
        whiteKingcheck = check_knight(board, y, x, "black")
      if board[y][x] == "r" and not whiteKingcheck:
        whiteKingcheck = check_rook(board, y, x, "black")
      if board[y][x] == "b" and not whiteKingcheck:
        whiteKingcheck = check_bishop(board, y, x, "black")
      if board[y][x] == "q" and not whiteKingcheck:
        whiteKingcheck = check_rook(board, y, x, "black")
        if not whiteKingcheck: whiteKingcheck = check_bishop(board, y, x, "black")

      if board[y][x] == 'P' and not blackKingcheck:
        blackKingcheck = check_pawn(board, y, x, "white")
      if board[y][x] == 'K' and not blackKingcheck:
        blackKingcheck = check_king(board, y, x, "white")
      if board[y][x] == 'N' and not blackKingcheck:
        blackKingcheck = check_knight(board, y, x, "white")
      if board[y][x] == "R" and not blackKingcheck:
        blackKingcheck = check_rook(board, y, x, "white")
      if board[y][x] == "B" and not blackKingcheck:
        blackKingcheck = check_bishop(board, y, x, "white")
      if board[y][x] == "Q" and not blackKingcheck:
        blackKingcheck = check_rook(board, y, x, "white")
        if not blackKingcheck: blackKingcheck = check_bishop(board, y, x, "white")
  return blackKingcheck, whiteKingcheck

def read_input():
  gn = 1
  try:
    while True:
      board = []
      for x in range(8):
        board += [list(input().strip())]

      if board == end_board: break

      bKing, wKing = check_pieces(board)

      if bKing: print ("Game #{}: black king is in check.".format(gn))
      if wKing: print ("Game #{}: white king is in check.".format(gn))
      if not bKing and not wKing: print ("Game #{}: no king is in check.".format(gn))

      
      input()
      gn += 1
  except EOFError: pass

read_input()