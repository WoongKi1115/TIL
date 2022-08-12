def get_prime(n):
    arr = [True] * (n + 1)

    for i in range(2, n):
        if arr[i]:
            for j in range(i + i, n + 1, i):
                arr[j] = False
    return [i for i in range(2, n + 1) if arr[i] == True]


X = get_prime(1000001)

T = int(input())
for tc in range(1, T + 1):
    D, A, B = map(int, input().split())
    count = 0
    list1 = []
    for i in X:
        if A <= i <= B:
            list1 += [i]


    for j in range(len(list1)):
        if str(D) in (str(list1[j])):
            count += 1
    print(f"#{tc} {count}")
