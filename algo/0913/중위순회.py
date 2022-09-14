def inorder(n):
    if len(box[n]) == 4:
        inorder(int(box[n][2]))
        print(box[n][1], end = '')
        inorder(int(box[n][3]))
    elif len(box[n]) == 3:
        inorder(int(box[n][2]))
        print(box[n][1], end = '')
    else:
        print(box[n][1], end = '')
    return

# 전위순회면 print가 첫줄
# 중위순회면 print가 가운데
# 후위순회면 print가 마지막줄에 들어가야함.
T = 10
for tc in range(1, T+1):
    N = int(input())
    box = [0]+[list(input().split()) for _ in range(N)]
    print(f"#{tc}", end = ' ')
    inorder(1)
    print()