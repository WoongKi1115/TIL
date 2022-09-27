def merge(left, right):
    global cnt
    merged_m = []
    l = r = 0

    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_m.append(left[l])
            l += 1
        else:
            merged_m.append(right[r])
            r += 1
    merged_m += left[l:]
    merged_m += right[r:]
    return merged_m


def merge_sort(m):
    global cnt
    if len(m) < 2:
        return m

    mid = len(m) // 2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list1 = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(list1)
    print(f"#{tc} {result[N//2]} {cnt}")
