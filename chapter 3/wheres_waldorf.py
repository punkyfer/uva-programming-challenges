def check_letters(y,x,char, chargrid):
    states = []
    for xmod in [-1,0,1]:
        for ymod in [-1,0,1]:
            newx, newy = x+xmod, y+ymod
            if newx >= 0 and newx<len(chargrid[y]) and newy>=0 and newy<len(chargrid):
                if chargrid[newy][newx] == char:
                    states.append((newy, newx))
    return states
                
def check_word(y,x, word, chargrid):
    states = check_letters(y,x, word[1], chargrid)
    found_direction = []
    for state in states:
        direction = [state[0]-y, state[1]-x]
        newx, newy = state[1], state[0]
        found = True
        for z in range(len(word)):
            if z>=2:
                newx, newy = newx+direction[1], newy+direction[0]
                if newx >= 0 and newx<len(chargrid[y]) and newy>=0 and newy<len(chargrid):
                    if chargrid[newy][newx] != word[z]:
                        found=False
                        break
                else:
                    found=False
                    break
        if found:
            found_direction.append(direction)
    return found_direction


def find_word(word, chargrid):
    for y in range(len(chargrid)):
        for x in range(len(chargrid[y])):
            if chargrid[y][x] == word[0]:
                if len(word)>1:
                    if len(check_word(y,x,word, chargrid))>0:
                        return (y+1,x+1)
                else:
                    return (y+1, x+1)
    return False

def read_input():
    try:
        num_cases = int(input().strip())
        cases = [[] for x in range(num_cases)]
        for x in range(num_cases):
            aux_line = input().strip()
            while (aux_line==""):
                aux_line = input().strip()
            num_lines = [int(a) for a in aux_line.split(" ")]
            cases[x] = [[],[]]
            for y in range(num_lines[0]):
                cases[x][0].append(list(input().strip().lower()))
            num_words = int(input().strip())
            for y in range(num_words):
                cases[x][1].append(input().strip().lower())
    except EOFError:
        pass
    return cases

cases = read_input()

for i,case in enumerate(cases):
    for word in case[1]:
        word_coords = find_word(word, case[0])
        print (word_coords[0], word_coords[1])
    if i < len(cases)-1:
        print()