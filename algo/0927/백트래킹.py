t = int(input())


def start(s, e, c):
    global cnt
    if s + e >= N - 1:
        cnt.append(c)
        return
    else:
        f = []
        for i in range(s + 1, s + e + 1):
            f.append([i, M[i], i + M[i]])
            #
            # c += 1
            # start(i, M[i], c)
            # c -= 1
        f.sort(key=lambda x: x[2])
        find_max_move = f[-1]

        start(find_max_move[0], find_max_move[1],c + 1)

for tc in range(1, 1 + t):
    n = list(map(int, input().split()))
    N = n[0]
    M = n[1:]
    start_index = 0
    start_num = M[0]
    cnt = []
    start(0, M[0], 0)
    print(f'#{tc} {min(cnt)}')
