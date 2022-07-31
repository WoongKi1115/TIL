#1. 전체 점수 합 계산하는 함수 total
def total(x):
    a = 0         # 합계를 저장해줄 변수를 만듬.
    for i in x:
        a += i     #a 값에 i 값을 더해줌
    return a

b = [80,90,85,75]
print(total(b))
