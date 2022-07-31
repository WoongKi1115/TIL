# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
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
        return True    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
