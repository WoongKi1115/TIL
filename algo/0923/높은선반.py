T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())           # B는 선반 높이
    height = list(map(int, input().split()))
    result = 100000
    for i in range(1<<N):
        sum_num = 0
        for j in range(N):
            if i & (1<<j):
                sum_num += height[j]
        if 0< sum_num-B < result:
            result = sum_num -B
    print(f"#{tc} {result}")

