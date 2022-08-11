arr = list(range(1,13))
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    result = 0
    for i in range(1<<len(arr)):
        count = 0
        sum_num = 0

        for j in range(len(arr)):
            if i&(1<<j):
                count += 1
                sum_num += arr[j]
        if count == N and sum_num == K:
            result += 1

    print(f"#{tc} {result}")
