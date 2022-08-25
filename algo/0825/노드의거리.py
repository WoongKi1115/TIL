T = int(input())
def bfs(s,g):
    visited[s] = 1
    queue = []
    queue.append(s)
    count = 0
    while queue:
        size = len(queue)
        count += 1
        for _ in range(size):
            t = queue.pop(0)
            for i in box[t]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1
                    # print(queue)
                    # print(visited)
                    # print("---")
        if visited[g] == 1:
            return count

    if visited[g] == 0:
        count = 0
        return count
for tc in range(1,T+1):
    V, E = map(int,input().split())
    box = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int,input().split())
        box[a].append(b)
        box[b].append(a)
    S, G = map(int,input().split())
    visited = [0]*(V+1)
    print(f"#{tc} {bfs(S,G)}")
    # print(box)
    # print(visited)