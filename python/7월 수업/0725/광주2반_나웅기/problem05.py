# 비밀번호 체크

def check_password_length(x):
    a = str(x)             #만약 비밀번호가 숫자로 주어질 수 있으니까 문자열로 바꿔줌
    if 8 <= len(a) <=32:   #x의 길이가 8보다 크거나 같고, 32보다 작거나 같다면 true
        return True
    else:
        return False  #아니면 false

a = '1231231231'
print(check_password_length(a))