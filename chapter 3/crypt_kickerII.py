tqbf = "the quick brown fox jumps over the lazy dog"
tqbf_len = 35

def get_phrase_len_value(phrase):
    if phrase[0:3] == phrase[-12:-9]:
        return sum( len(x) for x in phrase.split(" "))
    else:
        return 0

def read_input():
    num_cases = int(input().strip())
    input()
    cases = [[] for x in range(num_cases)]
    for x in range(num_cases):
        while (True):
            try:
                aux_line = input().strip()
                if (aux_line==""):
                    break
                else:
                    cases[x].append(aux_line)
            except EOFError:
                break
    return num_cases, cases

def conversion_dictionary(phrases):
    conversion_dict = {}
    for phrase in phrases:
        if get_phrase_len_value(phrase) == tqbf_len:
            for i, char in enumerate(phrase):
                if char != " ":
                    if char not in conversion_dict.keys():
                        conversion_dict[char] = tqbf[i]
    if len(conversion_dict) == 0:
        return False, "No solution."
    else:
        return True, conversion_dict

def convert_phrases(phrases, conversion_dict):
    new_phrases =  []
    try:
        for phrase in phrases:
            phrase_aux = ""
            for char in phrase:
                if char != " ":
                    phrase_aux += conversion_dict[char]
                else:
                    phrase_aux += " "
            new_phrases.append(phrase_aux)
    except:
        return ["No solution."]
    return new_phrases


num_cases, cases = read_input()

for i,case in enumerate(cases):
    state, conversion_dict = conversion_dictionary(case)
    if state:
        phrases = convert_phrases(case, conversion_dict)
        for phrase in phrases:
            print (phrase)
    else:
        print (conversion_dict)
    if i < (num_cases-1):
        print ("")

