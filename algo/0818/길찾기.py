T = 10
def dfs(v):
    visited[v] = 1
    for w in range(1, 101):
        if adjList[v][w] == 1 and visited[w] == 0:
            dfs(w)

for i in range(T):
    tc, num = map(int, input().split())
    list1 = list(map(int, input().split()))
    adjList = [[0] * 101 for _ in range(101)]
    for i in range(0, num * 2, 2):
        a = list1[i]
        b = list1[i + 1]
        adjList[a][b] = 1
    visited = [0] * 101

    dfs(0)
    if visited[99] == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
