T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    ci = list(map(int,input().split()))
    q = []
    for i in range(1, N+1):
        q.append([i, ci[0]])
        ci.pop(0)
    num = N+1
    while True:
        for _ in range(N):
            # print(q)
            # print('------')
            if q[0][1]//2 != 0:
                char = q.pop(0)
                char[1] = char[1]//2
                q.append(char)
            else:
                q.pop(0)
                if len(ci) != 0:
                    q.append([num, ci[0]])
                    num += 1
                    ci.pop(0)
                elif len(q) == 1:
                    break
        if len(q) == 1:
            print(f"#{tc} {q[0][0]}")
            break

