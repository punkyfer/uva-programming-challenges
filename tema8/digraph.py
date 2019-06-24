def find_max(graph):
    maxv, maxn = 0, -1
    for i,row in enumerate(graph):
        tmp = sum(row)
        if tmp > maxv:
            maxv = tmp
            maxn = i
    return maxn


def min_nodes(graph):

    solution = []
    visited = set()
    node = find_max(graph)

    while(len(visited) < len(graph)):
        visited.add(node)
        for i, col in enumerate(graph[node]):
            if col == 1:
                graph[node][i] = 0
                graph[i][node] = 0
                for row in range(len(graph)):
                    graph[row][i] = 0
                visited.add(i)
        solution.add(node)
        node = find_max(graph)

    return solution

def read_input():
    ctr = 0
    while True:
        n, m = (int(x) for x in input().split())
        if n+m == 0: break
        graph = [[0]*n for i in range(n)]

        for k in range(m):
            t1, t2 = (int(x)-1 for x in input().split())
            graph[t1][t2] = 1
            graph[t2][t1] = 1

        print (len(min_nodes(graph)))
        
        input()

if __name__ == "__main__":
    read_input()
    print()