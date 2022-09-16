def Trees_plus():
    global tree
    global x
    while x != 0:
        if x*2 +1 <= N:
            tree[x] = tree[x*2] + tree[x*2+1]
        else:
            tree[x] = tree[x* 2]
        x -= 1

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())  # N : 노드 수, M : 리프노드 수, L : 값을 추력할 노드 번호
    tree = [0] * (N+1)

    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b
    x = N - M
    Trees_plus()
    print(f"#{tc} {tree[L]}")
