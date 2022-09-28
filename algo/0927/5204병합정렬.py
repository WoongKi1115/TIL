T = int(input())


# m : 정렬 대상 배열
def merge_sort(m):
    if len(m) == 1:
        return m

    # 왼쪽 : left, 오른쪽 : right
    left = right = []
    # 가운데
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 왼쪽 오른쪽 분할 정복
    left = merge_sort(left)
    right = merge_sort(right)

    # 합친 결과 return
    return merge(left, right)


def merge(left, right):
    global cnt

    # 합병하기 전에
    # left 제일끝, right의 제일끝 비교
    if left[len(left) - 1] > right[len(right) - 1]:
        cnt += 1

    ln = len(left)  # 0 <= li < ln
    rn = len(right)  # 0 <= ri < rn

    # 왼쪽에서 다음에 꺼내올 원소의 위치 : li
    # 오른쪽에서 다음에 꺼내올 원소의 위치 : ri
    li = ri = 0
    result = []
    while li < ln or ri < rn:
        if li < ln and ri < rn:
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        elif li < ln:
            result.append(left[li])
            li += 1
        elif ri < rn:
            result.append(right[ri])
            ri += 1

    return result


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    # 왼쪽 부분의 제일 오른쪽이
    # 오른쪽 부분의 제일 오른쪽보다 클때 갯수 세기
    sorted_arr = merge_sort(arr)

    print(f"#{tc} {sorted_arr[N // 2]} {cnt}")
