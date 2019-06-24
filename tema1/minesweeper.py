n,m = 1,1
num_field = 0
while True:
    aux_line = input().strip()
    while aux_line == "":
        aux_line = input().strip()
    aux_line = aux_line.split(" ")
    n, m = int(aux_line[0]), int(aux_line[1])
    if n==m==0: break
    num_field += 1
    field = [[0 for col in range(m)] for row in range(n)]
    for row in range(n):
        line = input().strip()
        for col in range(m):
            if line[col]=="*":
                field[row][col] = "*"
                positions = [(row+1,col+1),(row+1,col),(row+1,col-1),(row-1,col+1),(row-1,col),(row-1,col-1),(row,col+1),(row,col-1)]
                positions = [ x for x in positions if 0<=x[0]<n and 0<=x[1]<m]
                for pos in positions:
                    if field[pos[0]][pos[1]] != "*":
                        field[pos[0]][pos[1]] += 1
                    
    print ("Field #"+str(num_field)+":")
    for i,line in enumerate(field):
        for item in line:
            print (item, end="")
        print()
    
    print()
    
