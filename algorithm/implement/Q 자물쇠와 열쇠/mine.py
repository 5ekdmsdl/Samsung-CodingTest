def solution(key, lock):
    answer = True
    graph = key
    for i in range(4):
        graph = turn(graph)
        for l in range(3):
            graph = lefr(graph)
            for r in range(3):
                graph = right(graph)
                for u in range(3):
                    graph = up(graph)
                    for d in range(3):
                        graph = down(graph)
                        
                        
    return answer


def turn(key):
    graph1 = [[0]*M for _ in range(M)]
    graph2 = key
    for i in range(M):
        graph1[i] = graph2[M-i-1]
    for i in range(M):
        for j in range(M):
            graph2[j][i] = graph1[i][j]
    return graph2

def left(key):
    graph = [[0]*n for _ in range(n)]
    for i in range(1,M):
        for j in range(M):
            graph[j][i-1] = key[j][i]
    return graph

def right(key):
    graph = [[0]*n for _ in range(n)]
    for i in range(1,M):
        for j in range(M):
            graph[j][i+1] = key[j][i]
    return graph

def up(key):
    graph = [[0]*n for _ in range(n)]
    for i in range(1,M):
        for j in range(M):
            graph[i-1][j] = key[i][j]
    return graph

def down(key):
    graph = [[0]*n for _ in range(n)]
    for i in range(1,M):
        for j in range(M):
            graph[i+1][j] = key[i][j]
    return graph
