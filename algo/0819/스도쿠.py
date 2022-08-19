T = int(input())
for tc in range(1, T + 1):
    box = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):  # 가로줄 확인
        count = [0] * 10
        for j in range(9):
            for x in range(1, 10):
                if box[i][j] == x:
                    count[x] += 1
        for a in range(1, 10):
            if count[a] != 1:
                result = 0

    for j in range(9):
        count = [0] * 10
        for i in range(9):
            for x in range(1, 10):
                if box[i][j] == x:
                    count[x] += 1
        for a in range(1, 10):
            if count[a] != 1:
                result = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * 10
            for x in range(1, 10):
                for y in range(3):
                    for z in range(3):
                        if box[i + y][j+z] == x and count[x] == 0:
                            count[x] += 1
        for a in range(1, 10):
            if count[a] != 1:
                result = 0

    print(f"#{tc} {result}")