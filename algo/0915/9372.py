def visiting(n):
    now = n
    visited = [0]*(N+1)
    visited[now] = 1
    stack = []
    count = 0
    while True:
        for i in range(1, N+1):
            if box[now][i] == 1 and visited[i] == 0:
                stack.append(now)
                count += 1
                visited[i] = 1
                now = i
                break
        else:
            if stack:
                now = stack.pop()
            else:
                break
    return count



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    box = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        box[a][b] = 1
        box[b][a] = 1
    result = []
    for i in range(1, N+1):
        result.append(visiting(i))
    print(min(result))