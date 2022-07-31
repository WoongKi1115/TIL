import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')


    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    #1-1 숫자 입력 받기(무조건 정수입력가정)
    while True:
        print()
        number = int(input('1이상 10000이하의 숫자를 입력하세요 :'))
    #1-2 범위 바깥 숫자를 입력했을 때, 잘못되었다고 알려준 후 다음 1-1로 돌아간다.
        if number > 10000 or number < 1:
            print('다시 입력해주세요.') 
            continue #continue는 while로 돌아가므로 while을 사이에 하나 더 생성시켜서 거기까지만 반복하게함
    #2-1 플레이어가 입력한 숫자와 정답과 비교하여 up, down 출력
    #number : 플레이어가 입력한 숫자
    #answer : 정답
        counts += 1

        if number > answer:
            print("Down!!!")
        elif number < answer:
            print("up!!!")
        else:
            print(f"Correct!! {counts}회 만에 정답을 맞히셨습니다.")
            
            print()
            break #정답 맞힌경우 반복문 종료
    #3 게임 재시작 여부 묻는 문구 출력
    command = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. : ')
    if command == 'y':
        continue
        print()
    elif command == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료하겠습니다.')
        
    else:
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
        
    is_playing = False
        #3-3 n을 입력받으면 게임을 종료
        #3-4 y와 n 이외의 다른 문자를 입력받으면 종료

