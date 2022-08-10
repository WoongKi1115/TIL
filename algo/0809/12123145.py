T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
     
    d = int(input())
     
    h_list = list(map(int,input().split()))
     
    cnt_list = [0]*100
     
    for i in range(100):
         
        cnt_list[h_list[i]-1] += 1
     
    while d:
         
        sort_h_list = [0]*100
         
        acc_cnt_list = cnt_list[:]
         
        for i in range(1,100):
             
            acc_cnt_list[i] += acc_cnt_list[i-1]
         
        for i in range(99,-1,-1):
             
            sort_h_list[acc_cnt_list[h_list[i]-1]-1] = h_list[i]
             
            acc_cnt_list[h_list[i]-1] -= 1
         
        h_list = sort_h_list[:]
         
        cnt_list[h_list[-1]-1] -= 1
         
        cnt_list[h_list[0]-1] -= 1
         
        h_list[-1] -= 1
         
        cnt_list[h_list[-1]-1] += 1
 
        h_list[0] += 1
         
        cnt_list[h_list[0]-1] += 1
         
        if h_list[0] >= h_list[-1]:
             
            break
 
        d -= 1
     
    sort_h_list = [0]*100
         
    acc_cnt_list = cnt_list[:]
 
    for i in range(1,100):
 
        acc_cnt_list[i] += acc_cnt_list[i-1]
 
    for i in range(99,-1,-1):
 
        sort_h_list[acc_cnt_list[h_list[i]-1]-1] = h_list[i]
 
        acc_cnt_list[h_list[i]-1] -= 1
     
    print('#'+str(t),sort_h_list[-1]-sort_h_list[0],sep=' ')