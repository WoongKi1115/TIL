# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    a = ''
    while True:
        if n//2 != 0:     #만약 n/2의 몫이 0이 아니라면
            a = a+str(n%2)  #a에 문자열 n/2의 나머지를 추가.
            n = n//2      #n은 n/2의 몫으로 변환.
            if n == 1:     #만약 n이 1이라면 
                a = a+str(1)  #a에 문자열 1추가
            elif n == 0:    #n이 0이라면
                a = a+str(0)  #문자열에 0추가
        else:
            break
    return a[::-1]        #a를 역방향으로 출력
      

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010