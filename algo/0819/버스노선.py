T = int(input())
for tc in range(1,T+1):
    N = int(input())              # 버스 노선의 개수
    line = []
    for _ in range(N):            # 노선들 받아옴
        a, b = map(int, input().split())
        line.append([a,b])
    P = int(input())
    count = [0] * (P+1)
    station = []
    for _ in range(P):
        x = int(input())
        station.append(x)

    for i in range(N):
        for j in range(line[i][0],line[i][1]+1):
            count[j] += 1
    result = []
    for x in station:
        result.append(count[x])
    print(f"#{tc} ",end='')
    for y in result:
        print(y, end=' ')
    print()


