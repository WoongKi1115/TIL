# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    a = list(word)    #문자열 x를 리스트로 쪼갬
    b = []   # 빈 리스트 추가(숫자로 바꾼 아스키 코드를 저장하기 위함)
    c = ''   # 빈 리스트 추가(다시 문자로 바꾼 아스키코드를 저장하기 위함.)
    for i in a:
        if ord(i)+n > 122:
            b.append(ord(i)+n-122+65)
        else:
            b.append(ord(i)+n)     #숫자로 바꾼 아스키코드에 양의 정수를 더해줌
        
    for j in b:
        c = c + chr(j)         #양의 정수를 더한 아스키코드를 문자로 바꾸어서 문자열로 만들어줌.
    return c

        


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx