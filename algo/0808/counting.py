x = [0,4,1,3,1,2,4,1]
D = [0]*8
count = [0]*5
for i in range(len(x)):
    count[x[i]] += 1

for i in range(1,len(count)):
    count[i] += count[i-1]
print(count)
for i in range(len(x)-1,-1,-1):
    count[x[i]] -= 1
    D[count[x[i]]] = x[i]
print(D)
