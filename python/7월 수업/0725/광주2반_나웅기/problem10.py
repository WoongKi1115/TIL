

def get_final_position(N,mat,moves):
    def found_position(N,mat):         # 현재 위치를 좌표로 알려줄 수 있는 함수를 만듬
        for i in range(N):     
            for j in range(N):         # mat 값에 1이 있는 것을 찾고 그 위치를 좌표로 출력.
                if mat[i][j] == 1:     #[[1, 0, 0], [0, 0, 0], [0, 0, 0]] 이 위치라면 (0,0)으로 나오게끔 만들어줌
                    return i, j        # (i,j)가 출력됨.
    a = list(found_position(N,mat))    # 출력된 i,j를 리스트로 바꾸어줌
    for i in moves:
        if i == 0:                     # moves에 주어진 이동방향이므로 해당 값이 떨어지면 그 위치로 이동하게끔 만듬.
            a[0] -= 1
        elif i == 1:
            a[0] += 1
        elif i == 2:
            a[1] -= 1
        elif i == 3:
            a[1] += 1

    if a[0] <0 or a[1] < 0 or a[0] > N or a[1] > N:   #위치가 좌표를 벗어나면 None가 나오게 만듬.
        return None
    else:
        return a                                      #위치가 좌표 내에 있다면 그 위치 값을 출력.

print(get_final_position(3,[[1, 0, 0], [0, 0, 0], [0, 0, 0]],[1, 1, 3]))
    

