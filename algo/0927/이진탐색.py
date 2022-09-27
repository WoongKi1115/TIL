def binarysearch(n, arr, key):
    global cnt
    left = 0
    right = n - 1
    flag =2
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            cnt += 1
            return mid
        elif arr[mid] > key:
            right = mid - 1
            if flag ==1:
                break
            else:
                if flag ==0 or flag ==2:
                    flag = 1
        else:
            left = mid + 1
            if flag ==0:
                break
            else:
                if flag==1 or flag==2:
                    flag =0

    return 0

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    box = [list(map(int,input().split())) for _ in range(2)]
    cnt = 0
    x = sorted(box[0])
    for i in box[1]:
        binarysearch(N, x, i)
    print(f"#{tc} {cnt}")