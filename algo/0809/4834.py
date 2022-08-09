T = int(input())
for tc in range(1, T+1):
    num = int(input())    #카드 장 수
    x = list(input())     # 뽑은 카드 수
    count = [0]*10        #카드가 몇 장씩 나왔는 지 세주기 위해서.
    a = [[0, 0]]          #a[0][0]에는 몇장이 나왔는지, a[0][1]에는 인덱스 값.
    for i in range(num):
        count[int(x[i])] += 1     #count의 인덱스 값이 카드의 값이므로 나올 때마다 1을 더해줌.
    for j in range(10):          # 카드가 0~9까지 이므로 range 10을 줌.
        if count[j] >= a[0][0]:     # a[0][0]이 나온 카드 수. 많이 나온 카드를 찾아야 함.
            a[0] = [count[j], j]    # a에 넣어줌.
    print(f"#{tc} {a[0][1]} {a[0][0]}")

# print(count)




