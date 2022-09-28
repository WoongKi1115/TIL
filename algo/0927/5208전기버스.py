T = int(input())


# idx : 현재 위치
# cnt : 충전 횟수
def backtracking(idx, cnt):
    global min_v

    if cnt >= min_v:
        return

    if idx == N - 1:
        min_v = min(min_v, cnt)
        return

    # 현재 위치에서 갈수 있는 곳 가기
    for i in range(1, bus_stop[idx] + 1):
        backtracking(idx + i, cnt + 1)


for tc in range(1, T + 1):
    line = list(map(int, input().split()))
    N = line[0]
    bus_stop = line[1:] + [0]
    min_v = 101

    backtracking(0, -1)

    print(f"#{tc} {min_v}")
