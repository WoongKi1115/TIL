N = 3  # 행
M = 4  # 열
# N개의 원소를 가진 0으로 초기화 된 1차원 배열
arr1 = [0] * N

# 크기가 NXM 이고 0으로 초기화된 2차원 배열
arr2 = [[0]*M for _ in range(N)]

# 아래의 방법은 불가능(얕은 복사가 됨)
arr3 = [[0]*M]*N
print(arr3)
arr3[0][0] = 1
print(arr3)

arr4 = [[1], [2, 3], [3, 4, 5]]
print(arr4)