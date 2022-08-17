def f(i, n): # i : 현재 단계, n : 목표 단계
    if i == n:
        return
    else:
        print(A[i])
        f(i + 1, n)

N = 3
A = [1,2,3]
f(0, N)