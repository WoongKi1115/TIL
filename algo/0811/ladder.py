di = [-1, 0, 0]
dj = [0, 1, -1]

T = 10
for tc in range(1, T + 1):
    t = int(input())
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    for i in range(102):
        if a[99][i] == 2:
            s = i

    d = 0
    x = 99
    while True:
        if x == 0:
            break
        if a[x][s - 1]:
            d = 2
            while True:
                x += di[d]
                s += dj[d]
                if a[x][s - 1] == 0:
                    break
        elif a[x][s + 1]:
            d = 1
            while True:
                x += di[d]
                s += dj[d]
                if a[x][s + 1] == 0:
                    break
        d = 0
        x += di[d]
        s += dj[d]

    print(f"#{tc} {s - 1}")

