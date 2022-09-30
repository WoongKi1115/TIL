def cal_s(a):
    si = 0
    for i in range(N//2):
        for j in range(i, N//2):
            si = box[i][j]

def dfs()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int,input().split())) for _ in range(N)]
