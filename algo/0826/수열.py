N, K = map(int,input().split())
list1 = list(map(int,input().split()))

sum1= sum(list1[0:K])
count = []
for i in range(N-K):
    sum1 = sum1 - list1[i] + list1[i+K]
    count.append(sum1)
print(max(count))
