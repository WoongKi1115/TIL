N = int(input())
for tc in range(1,N+1):
    problem = int(input())
    count = [0] * 6
    while True:
        if problem % 2 == 0:
            count[1] += 1
            problem = problem//2
        elif problem % 3 == 0:
            count[2] += 1
            problem = problem // 3
        elif problem % 5 == 0:
            count[3] += 1
            problem = problem // 5
        elif problem % 7 == 0:
            count[4] += 1
            problem = problem // 7
        elif problem % 11 == 0:
            count[5] += 1
            problem = problem // 11
        else:
            break
    print(f"#{tc}" ,end = ' ')
    for i in range(1, len(count)):
        print(count[i], end = ' ')
    print()