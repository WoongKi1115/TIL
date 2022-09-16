def dfs(i, j):
    global visited
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    stack = []
    stack.append((i,j))
    count = 1

    while stack:
        a = stack.pop()
        i = a[0]
        j = a[1]
        visited[i][j] = 1
        for d in range(4):
            ci = i + di[d]
            cj = j + dj[d]
            if 0<= ci < N and 0 <= cj< N and list1[ci][cj] == list1[i][j] + 1:
                i = ci
                j = cj
                stack.append((i,j))
                count += 1
                print(count, i, j)
                break
    return count

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list1 = [list(map(int,input().split())) for _ in range(N)]
    max_count = 0
    result = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                a = dfs(i, j)
                if max_count < a:
                    max_count = a
                    result = list1[i][j]
                elif max_count == a:
                    if result > list1[i][j]:
                        result = list1[i][j]

    print(f"#{tc} {result} {max_count}")
