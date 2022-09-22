import sys
sys.stdin = open("input1.txt", "r")
def Min_num(sumnum,i,j):
    global minnum
    if i == j == (N-1):
        sumnum += box[i][j]
        if sumnum < minnum:
            minnum = sumnum
    elif sumnum > minnum:
        return

    elif 0<=i<N and 0<=j<N:
        sumnum += box[i][j]
        Min_num(sumnum,i+1,j)
        Min_num(sumnum,i,j+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    sum_num = 0
    move = (N-1) * 2

    minnum = 1300
    Min_num(0,0,0)
    print(f"#{tc} {minnum}")