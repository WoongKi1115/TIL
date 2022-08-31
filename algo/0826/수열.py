N, K = map(int,input().split())
list1 = list(map(int,input().split()))
sum1 = 0
for i in range(K):
    sum1 += list1[i]
count = []
count.append(sum1)
for i in range(N-K):
    sum1 = sum1 - list1[i] + list1[i+K]
    count.append(sum1)
print(max(count))
