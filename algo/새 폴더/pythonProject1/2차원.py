T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    N = len(arr)  # 원소 개수
    exist = 0  # 부분집합의 합이 0이 될 때가 존재하면 1 아니면 0
    for i in range(1, 1 << N):  # 공집합이 안나오게 하기 위함.
        subset_sum = 0
        for j in range(N): # j = 0, 1, 2, 3, ... N-1
            if i & (1 << j):
                # i의 비트를 j 와 비교 list의 j 번 째 인덱스에 있는 원소가
                # 부분집합에 포함되어 있는지 검사
                # arr[j] 는 부분집합에 포함되어 있다.
                subset_sum += arr[j]
            exist = 1 if subset_sum == 0 else exist

    print(f"#{tc} {exist}")