def dfs(v, G):
    top = -1
    visited[v] = 1
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[w] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                return 0
        if v == G:
            return 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V + 1
    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)
    S, G = map(int, input().split())

    visited = [0] * N
    stack = [0] * N
    print(f"#{tc} {dfs(S, G)}")