#def caesar(x,n):  # x는 문자열, n은 양의 정수
    #a = list(x)    #문자열 x를 리스트로 쪼갬
    #b = []   # 빈 리스트 추가(숫자로 바꾼 아스키 코드를 저장하기 위함)
   # c = ''   # 빈 리스트 추가(다시 문자로 바꾼 아스키코드를 저장하기 위함.)
   # for i in a:
   #     b.append(ord(i)+n)     #숫자로 바꾼 아스키코드에 양의 정수를 더해줌
   # for j in b:
   #     c = c + chr(j)         #양의 정수를 더한 아스키코드를 문자로 바꾸어서 문자열로 만들어줌.
   # return c

        

def caesar(word,n):
    a = list(word) 
    for i in a:
        if a[i].isupper():
            a[i] = ((ord(a[i]) + n -65) % 26 + 65)      #대문자일 경우 아스키 코드의 범위 65 ~ 65 + 26
        elif a[i].islower():
            #소문자인 경우 아스키 코드 범위 97 ~ 97 + 26
            a[i] = ((ord(a[i]) + n -97) % 26 + 97)
        return ''.join(a)
    result = ''
    for char in word:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            char = (chr(ord(char) + n -65) % 26 + 65)
        elif char in "abcdefghijklmnopqrstuvwxyz":
            char = (chr(ord(char) + n -97) % 26 + 97)
            result += char
    return result

print(caesar('abc',3))

## git lab에 있음.