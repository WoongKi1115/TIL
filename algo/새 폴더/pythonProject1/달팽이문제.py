T = int(input())

for tc in range(1, T+1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]  # 0으로 채워진 2차원 배열 (n*n)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    d = 0  # 현재 채우는 방향

    value = 1
    ci, cj = 0, 0  # 현재 값을 채울 위치 i행 j열
    snail[ci][cj] = value

    # 반복을 통해 달팽이 채워나감
    # value 가 N*N이 될 때까지
    while value < N*N:
        # 현재 방향은 d에 저장됨.
        ni = ci + di[d]
        nj = cj + dj[d]
        # 가봤더니 인덱스 범위 벗어났거나
        # 아니면 내가 이미 채웠던 곳이라면 방향을 바꿈.
        # 갈 수 없으면 갈 수 있을 때까지 방향을 바꿔보면서 진행
        # 방향은 4번 까지 밖에 못바꿈.
        # 상하좌우가 막혀있으면 값 채우기가 끝났다를 의미. 반복문 종료
        for i in range(4):  # d = 0, 1, 2, 3  3에서 끝났다면 다시 0으로 가주어야함.
                            # 해결 방법
            d = (d+i)%4     # 나올 수 있는 값의 범위가 4로 나눈 나머지와 같음.
            # 다음 방향으로 가봄
            ni = ci + di[d]
            nj = cj + dj[d]

            if 0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0:
                # 갈 수 있는 방향을 찾으면 방향 바꾸기 종료
                ci = ni
                cj = nj
                break
        value += 1
        snail[ci][cj] = value

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()

