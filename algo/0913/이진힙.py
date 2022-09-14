def enq(n):
    global last
    last += 1
    heap[last] = n

    # 만약 새로 추가된 원소가 부모 노드보다 더 작은 경우 자리를 바꿔줘야함.
    c = last  # 새로 추가된 노드 (자식노드)
    p = c // 2  # 부모 노드

    # 부모가 존재하고, 부모보다 자식이 더 작으면 자리를 바꿈
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 혹시 바꾸고 난 다음에도 또 바꿔야할 수 있으니까
        # 부모와 자식을 바꿔준다..
        c = p
        p = c // 2

def heap_sum(n):
    # 중단 조건
    if n < 1:
        return 0

    result = heap[n]
    # 부모를 계속 거쳐가면서 언젠가 루트 노드에 도착하게 된다.
    return result + heap_sum(n//2)
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    list1 = list(map(int,input().split()))
    heap = [0] * (N+1)
    last = 0
    for i in list1:
        enq(i)

    print(f"#{tc} {heap_sum(N//2)}")