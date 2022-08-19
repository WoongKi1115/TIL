T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc}")
    x = N - 1

    for a in range(N):
        list1 = ['', '', '']
        for i in range(N - 1, -1, -1):
            list1[0] += str(box[i][a])
            list1[1] += str(box[x][i])
        for l in range(N):
            list1[2] += str(box[l][x])
        x -= 1
        print(f"{list1[0]} {list1[1]} {list1[2]}")
