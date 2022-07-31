#게임 캐릭터 움직일 수 있는 범위.
#n*n에서 이동,
#N = 3, M = 1, postion = (0,0)



def is_position_safe(N,M,position):
    a = list(position)             # 튜플 값으로 주어지므로 수정을 하기 위해서 리스트 값으로 바꿈.
    if M == 0:                     # M이 이동방향이므로 해당 값이 떨어지면 그 위치로 이동하게끔 만듬.
        a[0] -= 1
    elif M == 1:
        a[0] += 1
    elif M == 2:
        a[1] -= 1
    elif M == 3:
        a[1] += 1

    if a[0] <0 or a[1] < 0 or a[0] > N or a[1] > N:   #위치가 좌표를 벗어나면 False가 나오게 만듬.
        return False
    else:
        return True


print(is_position_safe(10,2,(5,5)))
