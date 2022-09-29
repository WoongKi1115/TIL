# dijkstra
def dijkstra(s, V):
    U = [0] * (V + 1)  # 비용이 결정된 정점 표시
    U[s] = 1  # 출발점 비용 결정함
    # D: 시작점에서 i번째 정점으로 가는데 걸리는 가중치의 합
    for i in range(V + 1):
        D[i] = adjM[s][i]

    # 정점의 비용 결정
    for _ in range(V + 1):
        # D[정점]가 최소인 w를 결정
        # 아직 비용이 결정되지 않은 정점 중에서 고르면 된다.
        u = 0
        minV = INF
        for i in range(V + 1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                u = i
        U[u] = 1  # 비용을 결정
        for v in range(V + 1):
            if 0 < adjM[u][v] < INF:
                D[v] = min(D[v], D[u] + adjM[u][v])


INF = 10000
V, E = map(int, input().split())
adjM = [[INF] * (V + 1) for _ in range(V + 1)]
# 자기 자신으로 가는 길은 0
for i in range(V + 1):
    adjM[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adjM[u][v] = w  # 유향그래프

D = [0] * (V + 1)  # 거리
dijkstra(0, V)
print(D)