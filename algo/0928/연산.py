from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    queue = deque([(n, 0)])
    visited = set()
    visited.add(n)

    while queue:
        n, cnt = queue.popleft()
        if n == m:
            break

        if n + 1 not in visited and n + 1 <= 1000000:
            queue.append((n + 1, cnt + 1))
            visited.add(n + 1)
        if n - 1 not in visited and n - 1 <= 1000000:
            queue.append((n - 1, cnt + 1))
            visited.add(n - 1)
        if n * 2 not in visited and n * 2 <= 1000000:
            queue.append((n * 2, cnt + 1))
            visited.add(n * 2)
        if n - 10 not in visited and n - 10 <= 1000000:
            queue.append((n - 10, cnt + 1))
            visited.add(n - 10)

    print(f'#{tc} {cnt}')