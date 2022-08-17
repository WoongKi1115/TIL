A = map(int,input().split())
for i in range(len(A)-1,0,-1):
    for j in range(0, i):
        if A[j] > A[j+1]:
            A[j], A[j+1] == A[j+1], A[j]
print(A[500000])