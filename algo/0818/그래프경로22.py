def dfs(v):
    visited = [0] * N
    visited[v] = 1
    for i in range(N):
        if visited[v] == 0 and adjList == 1:
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
    S, G = map(int, input().split())
    dfs(S)