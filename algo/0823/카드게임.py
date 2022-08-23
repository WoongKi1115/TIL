def tournament(i, j):
    if i == j:
        return i
    else:
        left = tournament(i, (i + j) // 2)
        right = tournament((i + j) // 2 + 1, j)
        return rsp(left, right)


def rsp(left, right):
    a = list1[left]
    b = list1[right]
    if a == 1:
        if b == 1:
            return left
        elif b == 2:
            return right
        elif b == 3:
            return left
    elif a == 2:
        if b == 1:
            return left
        elif b == 2:
            return left
        elif b == 3:
            return right
    elif a == 3:
        if b == 1:
            return right
        elif b == 2:
            return left
        elif b == 3:
            return left


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    list1 = list(map(int,input().split()))
    print(f"#{tc} {int(tournament(0, N-1))+1}")
