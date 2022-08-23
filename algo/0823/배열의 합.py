T = int(input())
def backtracking(r,sum):
    # 함수 안에서 전역변수를 사용하고 싶은 경우
    # 1. 수정하지 않고 읽기만 한다. => 그냥 쓰던대로 쓰면 됨.(파이썬 이름찾기 공식)
    # 2. 수정해야 한다 => 우리가 쓰던 대로 쓰면 전역변수가 아니라 지역변수가 되버림.
    # global 키워드로 전역변수를 사용한다고 선언 필요.
    global answer
    global visited

    if r == N:
        if answer > sum :
            answer = sum #우리가 구하는 것은 최소 합.
        return
    # 내가 알고 있는 최소합보다 현재합이 더 커버리면 더 진행할 필요가 없다.(가망이 없다)
    # 가망 없는 곳은 탐색하지 않도록 재귀 중단(가지치기)
    if sum > answer:
        return
    for c in range(N):
        if visited[c] == 0:
            visited[c] = 1
            sum += box[r][c]
            backtracking(r+1,sum += )
            visited[c] = 0


for tc in range(1,T+1):
    N = int(input())
    box = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 100
