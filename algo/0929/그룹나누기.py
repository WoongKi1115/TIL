T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    list1 = list(map(int, input().split()))
    counting = [0] * (N + 1)
    num = 0
    for i in range(0, len(list1), 2):
        if counting[list1[i]] != 0 and counting[list1[i + 1]] == 0:
            counting[list1[i + 1]] = counting[list1[i]]

        elif counting[list1[i + 1]] != 0 and counting[list1[i]] == 0:
            counting[list1[i]] = counting[list1[i + 1]]

        elif counting[list1[i + 1]] != 0 and counting[list1[i]] != 0:
            a, b = counting[list1[i + 1]], counting[list1[i]]
            for j in range(1, N + 1):
                if counting[j] == a or counting[j] == b:
                    counting[j] = a
        else:
            num += 1
            counting[list1[i]] = num
            counting[list1[i + 1]] = num

    counting2 = [0] * (N + 1)
    result = 0
    for j in range(1, N + 1):
        if counting[j] == 0:
            result += 1
        else:
            if counting2[counting[j]] == 0:
                counting2[counting[j]] = 1
                result += 1

    print(f"#{tc} {result}")
