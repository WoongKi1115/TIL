stack 가장 마지막에 추가된 자료부터 꺼내주는 자료구조 마지막 삽입된 원소 위치가 top(stack pointer)
top = -1 (지하라고 생각하면 됨.)
append, pop은 느림
때문에 stackpointer(top)을 활용하는게 나음.
stack = [0] * size 형식으로 스택 만들어서 활용.
push, pop 과정 전부 


스택 구현 고려사항
크기 예측이 필요.

재귀함수는 루프가 아님.
그냥 서로 다른 함수를 불러오는 것이라고 생각하면 됨.
```python
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```
f(i, n)  i 는 현재 단계, n은 목표(그만 부를 때의 목표치)


재귀함수의 중복으로 인한 느려짐 문제 해결 위해  
메모이제이션
매번 다시 계산하지 않도록 해서 전체적 실행 속도를 빠르게 하는 기술.