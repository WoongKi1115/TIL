di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


# 2차원 배열을 너비 우선 탐색으로 탐색하는 bfs 함수 작성
def bfs(si, sj, n):
    visited = [[0] * n for _ in range(n)]  # 2차원 배열
    queue = []
    queue.append((si, sj))
    visited[si][sj] = 1
    count = 0
    while queue:
        # 내가 현재 위치에서 방문을 몇번 할껀지 구하자.
        # 방문할 위치는 큐에 들어있고, 그 위치의 개수를 구하면 된다.
        size = len(queue)
        # 탐색 회수를 이전에 내가 알아낸 큐의 크기만큼만 하도록 제한하면
        # 해당 일차에만 반복을 하도록 제한할 수 있음.
        print(f"{count}일 차")
        print('=============')
        for a in range(n):
            print(visited[a])
        print('=============')
        for _ in range(size):
        # 현재 방문 위치 꺼내기
            i, j = queue.pop(0)

        # 현재 위치에서 갈 수 있는 곳 검사 (델타 이용한 4방향 탐색)
            for d in range(4):
                ni = di[d] + i
                nj = dj[d] + j
                # 다음 위치 알아내기 (행, 열)
                # 다음 위치가 탐색이 가능한 위치인지 검사(배열 범위를 벗어나지는 않았는지, 방문을 전에 한적이 있는지)
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    # 탐색이 가능한 위치라면
                    visited[ni][nj] = 1
                    # 방문 체크 하고
                    queue.append((ni, nj))
                # 다믕에 탐색 하기 위해 큐에 다음 위치를 추가
        count += 1

n = 10 # 10x10
print(bfs(5,5,10)) # 시작위치는 (5,5) 2차원 배열의 크기는 10*10