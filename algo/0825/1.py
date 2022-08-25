di = [-1, 1, 0, 0]  # 상하좌우
dj = [0, 0, -1, 1]


# 2차원 배열을 너비 우선 탐색으로 탐색하는 bfs 함수를 작성
def bfs(si, sj, n):  # n 은 2차원 배열의 크기, n * n
    visited = [[0] * n for _ in range(n)]  # 2차원 배열로 방문 체크
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1
    day = 0 # 몇일이 지났을까?
    while queue:
        # 내가 현재 위치에서 방문을 몇번 할껀지 구하자.
        # 방문할 위치는 큐에 들어있고, 그 위치의 개수(큐의 크기) 를 구하면 된다.
        size = len(queue)

        # 2차원 배열 모양 출력
        print(f"{day} 일차...")
        print("==========")
        for k in range(n):
            print(visited[k])
        print("==========")

        # 탐색 횟수를 이전에 내가 알아낸 큐의 크기만큼만 하도록 제한 하면
        # 해당 일차에만 반복을 하도록 제한 할 수 있다.
        for _ in range(size):
            # 현재 방문 위치 꺼내기
            i, j = queue.pop(0) # 맨 처음에서 꺼내야 하니까 pop(0)

            # 현재 위치에서 갈수 있는 곳 검사 (델타를 이용한 4방향 탐색)
            for d in range(4):
                # 다음 위치 알아내기 (행, 열)
                ni = i + di[d]  # 다음 행
                nj = j + dj[d]  # 다음 열
                # 다음 위치가 탐색이 가능한 위치인지 검사(배열 범위를 벗어나지는 않았는지, 방문을 전에 한적이 있는지)
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    # 탐색이 가능한 위치면
                    visited[ni][nj] = 1
                    # 방문 체크를 하고
                    queue.append((ni, nj))
                    # 다음에 탐색을 하기 위해 큐에 다음위치를 추가
        day += 1

n = 10 # 10 * 10
bfs(5,5,10) # 시작 위치는 (5,5), 2차원 배열의 크기는 10 * 10
