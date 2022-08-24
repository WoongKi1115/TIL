# r 번째 행에 대해서 몇번째 열에 있는 숫자를 고를까?
def backtracking(r, sum):
    # 함수안에서 전역변수를 사용하고 싶은경우
    # 1. 수정하지않고 읽기만 한다 ==> 그냥 쓰던대로 쓰면 됩니다. (파이썬의 이름 찾기 공식)
    # 2. 수정해야한다. ==> 우리가 쓰던대로 쓰면 전역변수가 아니라 지역변수가 되버린다.
    #    global 키워드로 전역변수를 사용한다고 꼭 선언
    # 전역변수로 쓰지 말고 함수의 파라미터로 다 가지고 다니는 방법
    global answer
    global visited

    if r == n:  # 다 고르고 나면 r이 2차원 배열의 크기만큼 되어있다. => 중단조건
        if answer > sum:
            answer = sum  # 우리가 구하는것은 최소 합
        return
        # 최소합 비교해서 저장

    # 내가 알고있는 최소 합보다 현재 합이 더 커버리면 더이상 진행할 필요가 없다. (가망이 없다.)
    # 가망 없는 곳은 탐색하지 않도록 재귀 중단(가지치기)
    if sum > answer:
        return

    # 열에 대해서 순회
    for c in range(n):
        # 이 전에 현재 열에 있는 숫자를 고른적이 있는지 검사
        if visited[c] == 0:
            # 전에 골랐던 열이랑 안겹치면 골랐다고 체크
            visited[c] = 1
            # 고른 수와 합을 구하고 다음 행으로 이동 (재귀)
            backtracking(r + 1, sum + arr[r][c])
            # 함수가 끝나고 나면 다시 돌아옴, 이번 열에 골랐다고 체크한것을 다시 원복
            visited[c] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    answer = 100  # 값 초기화
    backtracking(0, 0)  # 0 행부터, 합은 0부터 구하기 시작
    print(f"#{tc} {answer}")

