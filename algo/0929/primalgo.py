def prim1(r, V):
    MST = [0] * (V + 1)  # MST 포함여부
    key = [10000] * (V + 1)  # 가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결하는데 필요한 비용
    key[r] = 0  # 시작정점의 key
    # V+1개의 정점 중 V개를 선택
    for _ in range(V):
        # MST에 포함되지 않은 정점 중(MST[u]==0), key가 최소인 u 찾기
        u = 0
        minV = 10000
        for i in range(V + 1):
            if MST[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        MST[u] = 1  # 정점 u를 MST에 추가
        # u에 인접인 v에 대해, MST에 포함되지 않은 정점이면
        for v in range(V + 1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])  # u를 통해 MST에 포함되는 비용과 기존
    return sum(key)  # MST 가중치의 합

def prim2(r, V):
    MST = [0] * (V + 1)  # MST 포함여부
    MST[r] = 1  # 시작정점 표시
    s = 0  # MST 간선의 가중치 합
    for _ in range(V):
        u = 0
        minV = 10000
        # MST에 포함된 정점 i와 인접한 정점j 중 MST에 포함
        for i in range(V + 1):
            if MST[i] == 1:
                for j in range(V + 1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s


V, E = map(int, input().split())
adjM = [[0] * (V + 1) for _ in range(V + 1)]
adjL = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w
    adjM[v][u] = w
    adjL[u].append((v, w))
    adjL[v].append((u, w))

print(prim1(0, V))
print(prim2(0, V))