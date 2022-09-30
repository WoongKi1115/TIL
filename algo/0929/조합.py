def nci(i):
    # p의 i번째 칸을 채울 차례
    if i == N:
        print(p)
    else:
        # 채울 칸이 남았다.
        for j in range(1, N+1):
            if (used[j] == 0 and p[i-1] < j) or i == 0:
                used[j] = 1
                p[i] = j
                nci(i+1)
                used[j] = 0


N = int(input())    # N개의 숫자로 순열 만들기
p = [0] * N         # N개의 칸으로 이루어진
used = [0] * (N+1)  # 등장여부
nci(0)

