def read_input():
  num_words = int(input().strip())

  word_dict = []

  for i in range(num_words):
    word_dict += [input().strip()]

  enc_lines = []

  try:
    while True:
      line = input().strip()
      if not line: break
      enc_lines += [line]
  except EOFError: pass

  ck = CryptKicker(word_dict, enc_lines)

  return ck


class CryptKicker:

  def __init__(self, word_dict, enc_lines):
    self.word_dict = word_dict
    self.grouped_words = {}
    for word in word_dict:
      self.grouped_words.setdefault(len(word), []).append(word)
    self.enc_lines = enc_lines
    self.enc_words = []
    self.answer = {}

  def find_match(self, eword, dword, rel_table):
    for i, char in enumerate(eword):
      if char not in rel_table.keys():
        if dword[i] not in rel_table.values():
          rel_table[char] = dword[i]
        else:
          return False
      else:
        if rel_table[char] != dword[i]:
          return False
    return True

  def backtrack(self, rel_table, i):
    if i == len(self.enc_words): return True
    for word in self.grouped_words[len(self.enc_words[i])]:
      new_table = dict(rel_table)
      if self.find_match(self.enc_words[i], word, new_table):
        self.answer[self.enc_words[i]] = word 
        b = self.backtrack(new_table, i+1)
        if b: return True
    return False

  def decryptLines(self):
    for enc_line in self.enc_lines:
      self.enc_words = sorted(list(set(enc_line.split())), key=len, reverse=True)
      self.rel_table = {}
      self.all_chars = []

      new_line = ""
      rel_table = {}
      dec_possible = self.backtrack(rel_table, 0)
      split_line = enc_line.split()
      for i, word in enumerate(split_line):
        if not dec_possible:
          new_line += "*"*len(word)
        else:
          new_line += self.answer[word]
        if i < len(split_line)-1: new_line += " "

      print(new_line)





ck = read_input()
ck.decryptLines()