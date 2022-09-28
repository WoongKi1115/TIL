# 행 하나 증가 => 상태공간트리의 단계 증가
# 다음 행으로 간다 => 트리의 다음 단계로 간다
# board : 퀸이 놓인 상태
# remain : 남은 퀸 개수
def backtracking(row_num, board, remain):
    global cnt

    # 현재 행에서 i 열에 퀸을 놓을수 있는가>?
    for i in range(N):
        can_place = True
        # 세로 로 퀸이 있는지 검사
        for j in range(row_num):
            if board[j][i] == 1:
                can_place = False
                break
        # 대각선으로 퀸이 있는지 검사
        for j in range(1, row_num + 1):
            # 대각선 좌상
            if row_num - j >= 0 and i - j >= 0 and board[row_num - j][i - j] == 1:
                can_place = False
                break
            # 대각선 우상
            if row_num - j >= 0 and i + j < N and board[row_num - j][i + j] == 1:
                can_place = False
                break

        if can_place == True:
            board[row_num][i] = 1
            backtracking(row_num + 1, board, remain - 1)
            board[row_num][i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cnt = 0  # 경우의 수
    board = [[0] * N for _ in range(N)]
    backtracking(0, board, N)

    print(f"#{tc} {cnt}")