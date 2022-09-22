def enq(n):
    global last
    last += 1
    heap.append(n)
    c = last
    p = c//2

    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]

        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1]  # 루트 백업
    heap[1] = heap[last]  # 삭제할 노드의 키를 루트에 복사
    last -= 1  # 마지막 노드 삭제
    p = 1  # 루트에 옮긴 값을 자식과 비교
    c = p * 2   # 왼쪽 자식
    while c <= last:
        # print("p, c",p, c, heap[p], heap[c])
        # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
        if c+1 <= last and heap[c] > heap[c+1]:
            c += 1
        # 자식이 더 작으면 교환
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c   # 자식을 새로운 부모로
            c = p * 2   # 왼쪽 자식
        # 부모가 더 크면 중단
        else:
            break
    return tmp

N = int(input())
heap = [-1]
last = 0
for _ in range(N):
    x = int(input())
    if x == 0:
        if last == 0:
            print(0)
        else:
            print(deq())
            # heap.pop(1)
    else:
        enq(x)
    # print(heap)
    # print('last =',last)
