T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    N = len(B)
    M = len(A)
    i = 0
    j = 0
    count = 0
    while i < M and j < N:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == N:
            count += 1
            j = 0
        else:
            continue
    result = count + (M - N*count)
    print(f"{tc} {result}")
