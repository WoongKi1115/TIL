T = int(input())
for tc in range(1,T+1):
    x, y = map(int,input().split())
    box = [0] * (y)
    for i in range(y):
        box[i] = x//y
    if x%y != 0:
        for i in range(x%y):
            box[i] += 1

    result = 1
    for i in range(len(box)):
        result *= box[i]

    print(f"#{tc} {result}")