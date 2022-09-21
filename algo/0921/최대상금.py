def change(cnt):
    global max_num, count
    count += 1
    num = int(''.join(M))
    if (cnt,num) in check:
        return
    check.add((cnt, num))
    if cnt == N:
        if num > max_num:
            max_num = num
        return
    for i in range(len(M)-1):
        for j in range(i+1, len(M)):
            M[i], M[j] = M[j],M[i]
            change(cnt+1)
            M[i], M[j] = M[j], M[i]

T = int(input())
for tc in range(1, T+1):
    M, N = map(str, input().split())
    M = list(M)
    N = int(N)
    max_num = 0
    count = 0
    check = set()
    change(0)
    print(f"#{tc} {max_num}")
