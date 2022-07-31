print('=================================')
print('         Vending Machine         ')
print('=================================')
print('[Menu]')
print('1. 콜라 500원')
print('2. 사이다 700원')
print('3. 레모네이드 4500원')
print('4. 오렌지주스 2000원')
print('5. 초코우유 1200원')
print('6. 아메리카노 3600원')
print('=================================')

menus = ['콜라', '사이다', '레모네이드', '오렌지주스', '초코우유', '아메리카노']  # 메뉴 이름
costs = [500, 700, 4500, 2000, 1200, 3600]  # 메뉴 가격
budget = 0  # 자판기에 넣은 총 누적 금액

while True:
    print()
    #1-1. 금액 넣기
    money = int(input('금액을 넣어주세요.(그만 넣으시려면 0을 입력하세요.) : '))

    # 여기부터 코드를 작성하세요.
#1-4 0을 입력하면 반복문 탈출
#0일 때 입력을 그만받자 ==> 돈을 넣어달라고 더이상 말하지 않는다.
    if money == 0:
        break
    #1-3. 음수를 입력하면 문구 출력 후에 1-1로 돌아간다.
    if money < 0:
        print("금액은 1원 이상 넣어주세요.")
        continue
    #1-2. 금액 누적
    #금액을 넣을 때마다 누적 금액에 합산한다. 이후 처음으로 돌아간다.
    budget += money
    #budget = budget + money
    print(f"현재 누적 금액은 {budget}원 입니다.")

print()#한줄 띄우기

# 2. 메뉴 출력

# 2-1 지금까지 넣은 돈이 메뉴중에 제일 저렴한 메뉴의 가격보다 낮으면
#구매 가능한 메뉴가 없다 라고 출력한 다음 종료
if budget < 500:
    print(f"{budget}원으로 구매 가능한 메뉴가 없습니다.")
else:
    # 2-2
    # 구매 가능한 메뉴가 있다!!
    # 구매 가능한 메뉴 출력
    print(f"{budget}원으로 구매 가능한 메뉴는 다음과 같습니다.")

    #반복문
    for i in range(6):
        if costs[i] <= budget:
            print(f"{i+1}. {menus[i]} {costs[i]}원")

    print()
    # 3-1 구매할 메뉴 선택
    while True:
        print()
        choice = int(input('구매하실 메뉴의 번호를 입력하세요 : '))
    #구매 가능한 메뉴를 골랐다면 구매를 진행
        if 1 <= choice <= 6 and costs[choice - 1] <= budget:
            break
    #구매할 수 없는 메뉴를 골랐다면 구매할 수 없다고 출력한 뒤에 3-1로 돌아가야된다.
        print('구매할 수 없는 메뉴입니다.')
    
    print()
    #거스름돈 반환
    #4-1 어떤 메뉴를 선택했는지 출력
    print(f"{menus[choice -1]}를 구매하셨습니다.")

    print(f"거스름돈은 {budget - costs[choice-1]}원 입니다. 감사합니다.")