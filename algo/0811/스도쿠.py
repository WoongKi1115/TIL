T = int(input())
for tc in range(1, T+1):
    box = [list(map(int,input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        count = [0]*10
        for j in range(9):
            count[box[i][j]] += 1
        for x in range(1,10):
            if count[x] != 1:
                result = 0


    for j in range(9):
        count = [0]*10
        for i in range(9):
            count[box[j][i]] += 1
        for x in range(1,10):
            if count[x] != 1:
                result = 0


    for i in range(0,7,3):
        for j in range(0,7,3):
            count = [0]*10
            for a in range(3):
                for b in range(3):
                    =count[box[i+a][j+b]] + 1
            for x in range(1, 10):
                if count[x] != 1:
                    result = 0

    print(f"#{tc} {result}")

