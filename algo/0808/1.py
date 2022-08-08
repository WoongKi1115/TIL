T = int(input())

for t in range(1,T+1):
    case = int(input())

    scores = list(map(int,input().split()))
    max_count = 0   #최대 빈도수
    counts = [0]*101  # 점수 개수 세기. 점수의 범위는 0~100

    for score in scores:
        counts[score] += 1
        if max_count < counts[score]:
            max_count = counts[score]
        # max_count = counts[score] if max_count < counts[score] else max_count


    #최대 점수 구하기
    #빈도 수가 같다면 해당 점수가 1개든 2개든 다 구해줌.
    max_score = 0  #최대 빈도수 중 제일 큰 점수
    for score in range(len(counts)):
        if max_count == counts[score]:
            max_score=score  # score은 0부터 차례대로 증가 때문에 제일 마지막에 온 score 가 자동으로 최대 값 가짐
    print(f"#{case} {max_score}")