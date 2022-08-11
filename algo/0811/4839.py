T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    s = 1
    e = P
    count_A = 0
    count_B = 0
    while s <= e:
        c = int((s + e) // 2)
        if A > c:
            s = c
            count_A += 1
        elif A < c:
            e = c
            count_A += 1
        elif A == c:
            break
    s = 1
    e = P
    while s <= e:
        c = int((s + e) // 2)
        if B > c:
            s = c
            count_B += 1
        elif B < c:
            e = c
            count_B += 1
        elif B == c:
            break

    if count_A < count_B:
        print(f'#{tc} A')
    elif count_A > count_B:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')