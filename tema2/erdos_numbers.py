inf = "infinity"


aux_line = input()
while aux_line=="":
    aux_line = input()
num_scenarios = int(aux_line)
for scenario in range(num_scenarios):
    aux_line = input()
    while aux_line=="":
        aux_line = input()
    num_pa_au = aux_line.split(" ")
    
    ret_authors = int(num_pa_au[1].strip())
    num_papers = int(num_pa_au[0].strip())
    lines = []
    for np in range(num_papers):
        paper = input().split(":")
        line = []
        elements = paper[0].strip().split(",")
        for i,elem in enumerate(elements[:-1]):
            if "." not in elem:
                if "." in elements[i+1]:
                    line.append(elem.strip()+", "+elements[i+1].strip())
        lines.append(line)
    authors = {}
    for line in lines:
        for i,elem in enumerate(line):
            if elem in authors.keys():
                authors[elem] +=  line[:i]+line[(i+1):]
            else:
                authors[elem] =  line[:i]+line[(i+1):]
                    
    queue, visited = ["Erdos, P."], ["Erdos, P."]
    erdos_numbers={}
    erdos_numbers["Erdos, P."] = 0
    while queue:
        node = queue.pop(0)
        for elem in authors[node]:
            if elem not in visited:
                queue.append(elem)
                visited.append(elem)
                erdos_numbers[elem] = erdos_numbers[node]+1
        
    print ("Scenario "+str(scenario+1))
    for na in range(ret_authors):
        author = input()
        if author in erdos_numbers.keys():
            erdos_num = str(erdos_numbers[author])
        else:
            erdos_num = inf
        print (author+" "+erdos_num)

exit(0)