def run_inst(ptr, inst, reg, ram):
  ninst = int(inst / 100)
  a = int((inst % 100) / 10)
  b = int(inst % 10)
  if ninst==2: reg[a] = b
  elif ninst==3: reg[a] = (reg[a] + b) % 1000
  elif ninst==4: reg[a] = (reg[a] * b) % 1000
  elif ninst==5: reg[a] = reg[b]
  elif ninst==6: reg[a] = (reg[a] + reg[b]) % 1000
  elif ninst==7: reg[a] = (reg[a] * reg[b]) % 1000
  elif ninst==8: reg[a] = ram[reg[b]]
  elif ninst==9: ram[reg[b]] = reg[a]
  elif ninst==0: 
    if reg[b] != 0: return reg[a]
  return ptr+1

def count_instructions(reg, ram):
  num_inst = 1
  ptr = 0
  inst = ram[ptr]
  while inst != 100:
    ptr = run_inst(ptr, inst, reg, ram)
    inst = ram[ptr]
    num_inst += 1

  return num_inst

def read_input():
  try:
    num_cases = int(input().strip())
    input()
    for case in range(num_cases):
      reg = [0]*10
      ram = [0]*1000
      ctr = 0
      while True:
        aux = input()
        if aux == '\r': break
        ram[ctr] = int(aux)
        ctr += 1

      print(count_instructions(reg, ram))
      if case < num_cases-1: print()
  except EOFError: print(count_instructions(reg, ram))

read_input()