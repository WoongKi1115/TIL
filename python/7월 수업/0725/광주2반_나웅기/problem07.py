def dec_to_bin(number):
    if number < 2:
        return str(number)
    else:
        #2 이상의 수가 왔을 때
        #재귀함수 를 어떻게 호출할 것인지.
        # 이진수 구하는 방법
        # 몫이 2보다 작아질 때 까지 2로 계속 나눔
        # 나머지를 계속 알고있다가 몫이 2보다 작아진 순간 앞에서부터 차례대로
        # 문자열 이어주기.
        # 몫이 2보다 작아질 때까지 계속 2로 나누고 그 다음에 나머지를 더함.
        return dec_to_bin(number//2) + dec_to_bin(number%2)

print(dec_to_bin(55))