from collections import deque

# deque 이용

p = 1
q = deque()
n = 1000000
m = 0
v = 0

while m < n:
    q.append((p, 1, 0))
    v, c, my = q.popleft()  # 맨 왼쪽에서 원소 빼기
    m += 1
    q.append((v, c + 1, my + c))
    p += 1