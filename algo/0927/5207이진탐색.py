T = int(input())

R = 1
L = 0

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))  # 정렬 대상
    B = list(map(int, input().split()))  # 검색 대상

    A.sort()

    # 조건에 맞으면서, A안에서 찾은 B의 원소 개수
    cnt = 0
    # 조건은 이진 탐색 할때, 왼쪽 / 오른쪽
    # 이전에 왼쪽에 갔다가 또 왼쪽으로 가면 안된다.
    # 탐색 범위를 둘로 나눌때, 이전에 선택했던 범위로 다시 가면 안된다.
    for number in B:
        left = 0
        right = N - 1
        dir = -1  # 처음 시작할때는 방향이 없는 상태
        while left <= right:
            mid = (left + right) // 2
            # 답찾으면 개수 증가
            if A[mid] == number:
                cnt += 1
                break
            # 찾는 범위를 왼쪽으로 제한
            elif A[mid] > number:
                right = mid - 1
                # 내가 이전에 선택한 범위가 왼쪽이었다.
                # 조건 위반임!!
                # 탐색 중지하고 다음으로 넘어가기
                if dir == L:
                    break
                dir = L
            # 찾는 범위를 오른쪽으로 제한
            else:
                left = mid + 1
                # 내가 이전에 선택한 범위가 오른쪽이이었다.
                # 탐색 중지하고 다음으로 넘어가기
                if dir == R:
                    break
                dir = R

    print(f"#{tc} {cnt}")
