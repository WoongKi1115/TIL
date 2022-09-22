import heapq


N = int(input())
heap = [-1] * (N+1)
for _ in range(N):
    num = int(input())
    if num == 0:
        result = heapq.heappop(heap)
        if result == -1:
            print(0)
        else:
            print(result)
    else:
        heapq.heappush(heap, num)