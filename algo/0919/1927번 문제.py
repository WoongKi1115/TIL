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
    tem = heap[1]
    heap[1] = heap[last]

    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] > heap[c+1]:
            c += 1
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    last -= 1
    return tem

N = int(input())
heap = [0]
last = 0
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(deq())
            heap.pop(1)
    else:
        enq(x)
    print(heap)
    print('last =',last)
