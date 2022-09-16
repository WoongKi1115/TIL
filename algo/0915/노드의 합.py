def Trees_plus(n):
    global tree
    global x
    if n <= x:
        Trees_plus(n*2)
        Trees_plus(n*2+1)
        if n*2 +1 <= N:
            tree[n] = tree[n*2] + tree[n*2+1]
        else:
            tree[n] = tree[n * 2]

T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())  # N : 노드 수, M : 리프노드 수, L : 값을 추력할 노드 번호
    tree = [0] * (N+1)

    for _ in range(M):
        a, b = map(int,input().split())
        tree[a] = b
    x = N - M
    Trees_plus(1)
    print(f"#{tc} {tree[L]}")
