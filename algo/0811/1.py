T = int(input())
for tc in range(1, T+1):
    box = [list(map(int,input().split())) for _ in range(9)]

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            count = [0] * 10
            for a in range(3):
                for b in range(3):
                    count[box[i + a][j + b]] += 1
            print(count)