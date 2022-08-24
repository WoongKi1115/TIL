T = 10
for _ in range(1,T+1):
    tc = int(input())
    queue = list(map(int,input().split()))
    while True:
        for i in range(1,6):
            a = queue.pop(0)
            a -= i
            if a > 0:
                queue.append(a)
            else:
                a = 0
                queue.append(a)
                break

        if queue[-1] == 0:
            break


    print(f"#{tc}", end = ' ')
    for i in queue:
        print(i, end = ' ')
    print()

