#2. 전체 점수 평균 계산하는 함수
def average(x):
    a = 0
    for i in x: 
        a += i       #여기까지 합계 계산과 동일
    return a/len(x)   #평균을 계산하기 위해 리스트 길이로 나누어줌

b = [80,90,85,75]
print(average(b))

