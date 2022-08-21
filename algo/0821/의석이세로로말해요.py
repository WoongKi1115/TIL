T = int(input())
for tc in range(1,T+1):
    box = [list(input()) for _ in range(5)]
    print(f"#{tc}", end = ' ')
    for x in range(15):
        for y in range(5):
            if len(box[y]) > x:
                print(box[y][x], end = '')
    print()

