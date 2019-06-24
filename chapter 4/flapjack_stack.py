def read_input():
    stacks = []
    try:
        aux_line = input().strip()
        while (aux_line != None):
            stack = [int(x) for x in aux_line.split(" ")]
            stacks.append(stack)
            aux_line = input().strip()
    except EOFError:
        pass
    return stacks

def solve_stack(stack, flips=[], mod = 0):
  if (len(stack) == 1):
    return flips;
  else:
    stack_len = len(stack)-1
    max_pos = 0
    max_elem, t_pos = 0, 0
    for pos, elem in enumerate(stack):
      if elem > max_elem:
        max_elem, t_pos = elem, pos
    if max_pos == t_pos:
      return solve_stack(stack[1:], flips, mod+1)
    else:
      if(t_pos != stack_len):
        flips += [t_pos+1+mod]
        stack = stack[0 : t_pos] + stack[stack_len : t_pos-1 : -1]  
      flips += [1+mod]
      stack = stack[ : : -1]
      return solve_stack(stack[1:], flips, mod+1)


stacks = read_input()

for stack in stacks:
  print(*stack)
  stack_flips = solve_stack(stack[::-1], [], 0)+[0]
  print (*stack_flips)