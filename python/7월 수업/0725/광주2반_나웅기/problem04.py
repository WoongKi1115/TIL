#check_duplicate_id 함수
y = ['asdjfl;qwte','skdndrl','rlawhdrnr']
def check_duplicate_id(x,y):
    if x in y:                 # 신규 아이디 x가 기존 아이디 리스트 y 안에 있는지를 비교.
        return False           # 있다면 False. 없다면 True
    elif x not in y:
        return True

